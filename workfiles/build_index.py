import os
from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv('.env', override=True)

NEO4J_URI = os.getenv('NEO4J_URI')
NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Create the vector index
vector_index = Neo4jVector.from_existing_graph(
    embeddings = OpenAIEmbeddings(api_key=openai_api_key),
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    index_name='testcases',
    node_label="TestCase",
    text_node_properties=['prompt', 'testcase_name', 'response', 'documentation'],
    embedding_node_property='embedding',
)

print("Vector index built and stored in Neo4j.")