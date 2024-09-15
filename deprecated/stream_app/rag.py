import sys
import os
from openai import OpenAI

# Ensure the correct import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../utilities'))

from knowledge_graph import KnowledgeGraph
from config import config

# Modify the rag_pipeline function
def rag_pipeline(user_input, kg, ollama_llm):
    # Initialize Knowledge Graph
    kg = KnowledgeGraph()
    
    # Build the graph or query it as needed
    kg.create_node("Person", {"name": "John Doe", "age": 29})
    
    # Query the knowledge graph for relevant information
    # This is a placeholder - replace with actual querying logic
    kg_info = "Person: John Doe, Age: 29"
    
    # Close the connection to the graph
    kg.close()
    
    # Prepare the prompt for Llama, incorporating knowledge graph information
    prompt = f"""Based on the following user input and knowledge graph information, generate a response:
            User Input: {user_input}
            Knowledge Graph Information: {kg_info}
            Please provide a detailed and relevant response:
        """
    # Call Llama using the Ollama client
    try:
        response = ollama_llm(prompt)
        return response #.strip()
    except Exception as e:
        return f"Error in RAG pipeline: {str(e)}"

# Dummy function to represent calling the model endpoint
# Replace this with actual logic for calling your model
# def call_model_endpoint(user_input, model_endpoint):
#     return f"Model response for input: {user_input}"


# def rag_pipeline(user_input, kg, openai_client):
#     # Initialize Knowledge Graph
#     kg = KnowledgeGraph()
    
#     # Build the graph or query it as needed
#     kg.create_node("Person", {"name": "John Doe", "age": 29})
    
#     # Query the knowledge graph for relevant information
#     # This is a placeholder - replace with actual querying logic
#     kg_info = "Person: John Doe, Age: 29"
    
#     # Close the connection to the graph
#     kg.close()
    
#     # Prepare the prompt for GPT-4, incorporating knowledge graph information
#     prompt = f"""Based on the following user input and knowledge graph information, generate a response:

#             User Input: {user_input}

#             Knowledge Graph Information: {kg_info}

#             Please provide a detailed and relevant response:

#         """

#     # Call GPT-4 using the OpenAI client
#     try:
#         response = openai_client.chat.completions.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a helpful assistant with access to a knowledge graph."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.7,
#             max_tokens=1000
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"Error in RAG pipeline: {str(e)}"

# The call_model_endpoint function is no longer needed as we're directly using the OpenAI client
