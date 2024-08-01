import sys
import os

# Ensure the correct import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../utilities'))

from kg import KnowledgeGraph
from config import config

def rag_pipeline(user_input, kg, model_endpoint, test_case_type, uploaded_data=None):
    # Query the knowledge graph
    query_result = kg.query_graph(user_input)
    
    # Prepare context from query result
    context = "\n".join([f"Test Case: {record['testcase_name']}, Type: {record['testcase_type']}, Prompt: {record['prompt']}, Documentation: {record['documentation']}, Expected Response: {record['response']}" for record in query_result])
    
    # Combine user input with context
    enhanced_prompt = f"Context:\n{context}\n\nUser Query: Generate a {test_case_type} test case for {user_input}\n"
    
    if uploaded_data is not None and not uploaded_data.empty:
        enhanced_prompt += f"\nUse the following data for data-driven robot framework testcase generation:\n{uploaded_data.to_string(index=False)}"
    
    enhanced_prompt += "\nGenerate a detailed test case based on the context, user query, and any provided data:"
    
    # Call the model endpoint
    response = call_model_endpoint(enhanced_prompt, model_endpoint)
    
    return response

def call_model_endpoint(prompt, model_endpoint):
    # Implement the logic to call your model endpoint
    # This is a placeholder function
    return f"Model response for input: {prompt}"