import sys
import os

# Ensure the correct import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../utilities'))

from knowledge_graph import KnowledgeGraph
from config import config

def rag_pipeline(user_input, kg, model_endpoint):
    # Initialize Knowledge Graph
    kg = KnowledgeGraph()
    
    # Build the graph or query it as needed
    kg.create_node("Person", {"name": "John Doe", "age": 29})
    
    # Close the connection to the graph
    kg.close()
    
    # Assuming you call the model endpoint with user_input
    # Here, include logic to call the model endpoint and get the response
    # For example:
    # response = call_model_endpoint(user_input, model_endpoint)
    # return response

    # Placeholder response
    return "RAG pipeline executed successfully."

# Dummy function to represent calling the model endpoint
# Replace this with actual logic for calling your model
def call_model_endpoint(user_input, model_endpoint):
    return f"Model response for input: {user_input}"
