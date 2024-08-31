import os  
import sys
import pandas as pd
import streamlit as st
from neo4j import GraphDatabase
from contextlib import contextmanager

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, '../utilities'))

from config import config

@st.cache_resource
def get_neo4j_driver():
    return GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD), connection_timeout=60)

@st.cache_data
# def map_data_to_graph(data):
#     nodes = []
#     edges = []
#     for index, row in data.iterrows():
#         testcase_node = {
#             "name": row['TestcaseName'], 
#             "type": 'Testcase'
#         }
#         nodes.append(testcase_node)

#         if 'KeywordName' in row and pd.notna(row['KeywordName']):
#             keyword_node = {"name": row['KeywordName'], "type": "Keyword"}
#             nodes.append(keyword_node)
#             edges.append({
#                 "source": row['TestcaseName'], 
#                 "target": row['KeywordName'], 
#                 "relation": "HAS_STEP"
#             })

#             # Add arguments as separate nodes
#             for i in range(1, 4):
#                 arg_col = f'Argument{i}'
#                 if arg_col in row and pd.notna(row[arg_col]):
#                     arg_node = {"name": row[arg_col], "type": "Argument"}
#                     nodes.append(arg_node)
#                     edges.append({
#                         "source": row['KeywordName'],
#                         "target": row[arg_col],
#                         "relation": f"HAS_ARG_{i}"
#                     })

#         if 'Documentation' in row and pd.notna(row['Documentation']):
#             doc_node = {"name": row['Documentation'], "type": "Documentation"}
#             nodes.append(doc_node)
#             edges.append({
#                 "source": row['TestcaseName'],
#                 "target": row['Documentation'],
#                 "relation": "HAS_DOCUMENTATION"
#             })

#     return nodes, edges

def map_data_to_graph(data):
    nodes = []
    edges = []
    for index, row in data.iterrows():
        testcase_node = {
            "id": f"testcase_{index}",
            "name": row['TestcaseName'],
            "type": 'Testcase'
        }
        nodes.append(testcase_node)

        for col in data.columns:
            if col != 'TestcaseName':
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
        session.run("MATCH (n) DETACH DELETE n")
        
        for node in nodes:
            session.run(
                "CREATE (n:Node {id: $id, name: $name, type: $type})",
                id=node['id'], name=node['name'], type=node['type']
            )
        
        for edge in edges:
            session.run(
                """
                MATCH (a:Node {id: $source}), (b:Node {id: $target})
                CREATE (a)-[r:RELATES_TO {type: $relation}]->(b)
                """,
                source=edge['source'], target=edge['target'], relation=edge['relation']
            )

def get_test_case_structure(driver):
    with driver.session() as session:
        result = session.run("""
        MATCH (t:Node {type: 'Testcase'})-[r:RELATES_TO]->(n:Node)
        WITH t, collect({type: n.type, name: n.name, relation: r.type}) as properties
        RETURN t.name as TestCase, properties
        """)
        return [record for record in result]

def clear_neo4j_database(driver):
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")


# @contextmanager
# def get_db_session():
#     driver = get_neo4j_driver()
#     session = driver.session()
#     try:
#         yield session
#     finally:
#         session.close()

# @st.cache_data
# def update_neo4j_with_graph(nodes, edges):
#     with get_db_session() as session:
#         for node in nodes:
#             session.run(
#                 """
#                 MERGE (n {name: $name, type: $type})
#                 """, name=node['name'], type=node['type']
#             )
        
#         for edge in edges:
#             session.run(
#                 """
#                 MATCH (a {name: $source}), (b {name: $target})
#                 MERGE (a)-[r:%s]->(b)
#                 """ % edge['relation'], source=edge['source'], target=edge['target']
#             )

# @st.cache_data
# def clear_neo4j_database():
#     with get_db_session() as session:
#         session.run("MATCH (n) DETACH DELETE n")

# # Function to close the driver when the Streamlit app is shut down
# def close_neo4j_driver():
#     driver = get_neo4j_driver()
#     driver.close()

# # Register the close_neo4j_driver function to be called when the Streamlit app is shut down
# # Replace the deprecated cache clearing method with the appropriate one
# if 'clear_streamlit_cache' not in st.session_state:
#     st.session_state['clear_streamlit_cache'] = True
#     # Clear the caches using the public API
#     st.cache_data.clear()
#     st.cache_resource.clear()

# st.session_state['_neo4j_driver_closer'] = close_neo4j_driver