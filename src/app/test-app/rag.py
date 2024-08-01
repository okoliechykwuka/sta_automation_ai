from langchain.retrievers import KnowledgeGraphRetriever
from langchain.graphs import NetworkxEntityGraph
from knowledge_graph import KnowledgeGraph, create_networkx_graph
import os

def setup_rag():
    uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    user = os.getenv("NEO4J_USER", "neo4j")
    password = os.getenv("NEO4J_PASSWORD", "password")

    kg = KnowledgeGraph(uri, user, password)
    neo4j_graph = kg.get_graph()
    kg.close()

    G = create_networkx_graph(neo4j_graph)
    entity_graph = NetworkxEntityGraph(G)
    retriever = KnowledgeGraphRetriever(graph=entity_graph)
    return retriever

def query_knowledge_graph(retriever, query):
    return retriever.get_relevant_documents(query)