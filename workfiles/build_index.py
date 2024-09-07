import os
from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv('.env', override=True)

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')


# Create the vector index
vector_index = Neo4jVector.from_existing_graph(
    OpenAIEmbeddings(api_key="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"),
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    index_name='testcases',
    node_label="TestCase",
    text_node_properties=['prompt', 'testcase_name', 'response', 'documentation'],
    embedding_node_property='embedding',
)

print("Vector index built and stored in Neo4j.")