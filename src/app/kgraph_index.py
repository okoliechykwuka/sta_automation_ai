print(f"Loaded {__file__}")

import os
import sys
import pandas as pd
from neo4j import GraphDatabase
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings.openai import OpenAIEmbeddings
import streamlit as st
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the 'src' directory to sys.path
sys.path.append(os.path.join(current_dir, '..'))

from utilities.config import app_config

def get_neo4j_driver():
    try:
        return GraphDatabase.driver(
            app_config.NEO4J_URI, 
            auth=(app_config.NEO4J_USER, app_config.NEO4J_PASSWORD),
            connection_timeout=30,  # Increase the connection timeout to 30 seconds
            max_connection_lifetime=300  # Increase max connection lifetime to 600 seconds (10 minutes)
        )
    except Exception as e:
        print(f"Error creating Neo4j driver: {str(e)}")
        return None

def compute_embeddings_for_new_nodes(batch_size=100, max_retries=5, initial_retry_delay=5):
    embeddings = OpenAIEmbeddings(openai_api_key=app_config.OPENAI_API_KEY)
    driver = get_neo4j_driver()
    
    with driver.session() as session:
        result = session.run("""
        MATCH (n:TestCase)
        WHERE n.embedding IS NULL
        RETURN n.id AS id, n.prompt AS prompt, n.testcase_name AS testcase_name, n.response AS response, n.documentation AS documentation
        """)
        nodes = result.data()
        
    texts = []
    ids = []
    for node in nodes:
        text = ' '.join([
            node.get('prompt', ''),
            node.get('testcase_name', ''),
            node.get('response', ''),
            node.get('documentation', ''),
        ])
        texts.append(text)
        ids.append(node['id'])

    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i+batch_size]
        batch_ids = ids[i:i+batch_size]
        
        retry_delay = initial_retry_delay
        for retry in range(max_retries):
            try:
                embeddings_list = embeddings.embed_documents(batch_texts)
                
                with driver.session() as session:
                    for node_id, embedding_vector in zip(batch_ids, embeddings_list):
                        session.run("""
                        MATCH (n:TestCase {id: $id})
                        SET n.embedding = $embedding
                        """, id=node_id, embedding=embedding_vector)
                
                break  # Success, exit retry loop
            except Exception as e:
                if retry < max_retries - 1:
                    st.warning(f"Error computing embeddings: {e}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    st.error(f"Failed to compute embeddings after {max_retries} attempts: {e}")

def create_vector_index():
    compute_embeddings_for_new_nodes()

    return Neo4jVector.from_existing_graph(
        embedding=OpenAIEmbeddings(openai_api_key=app_config.OPENAI_API_KEY),
        url=app_config.NEO4J_URI,
        username=app_config.NEO4J_USER,
        password=app_config.NEO4J_PASSWORD,
        index_name='testcases',
        node_label="TestCase",
        text_node_properties=['prompt', 'testcase_name', 'response', 'documentation'],
        embedding_node_property='embedding'
    )

def map_data_to_graph(data):
    nodes = []
    edges = []
    for index, row in data.iterrows():
        testcase_node = {
            "id": f"testcase_{index}",
            "name": row['testcase_name'],
            "type": 'Testcase',
            "prompt": row.get('prompt', ''),
            "response": row.get('response', ''),
            "documentation": row.get('documentation', '')
        }
        nodes.append(testcase_node)

        for col in data.columns:
            if col not in ['testcase_name', 'prompt', 'response', 'documentation']:
                value = row[col]
                if pd.notna(value):
                    node = {
                        "id": f"{col}_{index}",
                        "name": str(value),
                        "type": col
                    }
                    nodes.append(node)
                    edges.append({
                        "source": testcase_node["id"],
                        "target": node["id"],
                        "relation": f"HAS_{col.upper()}"
                    })

    return nodes, edges

def update_neo4j_with_graph(driver, nodes, edges):
    with driver.session() as session:
        for node in nodes:
            session.run(
                """
                MERGE (n:Node {id: $id})
                SET n += $properties
                """,
                id=node['id'],
                properties=node
            )
        
        for edge in edges:
            session.run(
                """
                MATCH (a:Node {id: $source}), (b:Node {id: $target})
                MERGE (a)-[r:RELATES_TO {type: $relation}]->(b)
                """,
                source=edge['source'], target=edge['target'], relation=edge['relation']
            )

def get_test_case_structure(driver):
    with driver.session() as session:
        result = session.run("""
        MATCH (t:Node {type: 'Testcase'})-[r:RELATES_TO]->(n:Node)
        WITH t, collect({type: n.type, name: n.name, relation: r.type}) as properties
        RETURN t.name as TestCase, t.prompt as Prompt, t.response as Response, t.documentation as Documentation, properties
        """)
        return [record for record in result]

def clear_neo4j_database(driver):
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")

def add_prompt_to_graph(driver, prompt, response, testcase_name):
    with driver.session() as session:
        session.run(
            """
            CREATE (t:Node {id: $id, name: $name, type: 'Testcase', prompt: $prompt, response: $response})
            """,
            id=f"testcase_{testcase_name}", name=testcase_name,
            prompt=prompt, response=response
        )

def get_similar_testcases(vector_index, prompt, k=5):
    results = vector_index.similarity_search_with_score(prompt, k=k)
    return [(result[0].page_content, result[1]) for result in results]