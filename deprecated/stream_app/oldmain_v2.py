import sys
import os
import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
import plotly.express as px
import streamlit.components.v1 as components
from langchain_openai import OpenAI
import logging
from neo4j.exceptions import Neo4jError

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, '../utilities'))

from kgraph_index import (
    get_neo4j_driver, create_vector_index, map_data_to_graph, 
    update_neo4j_with_graph, clear_neo4j_database, add_prompt_to_graph,
    get_similar_testcases, get_test_case_structure
)
from baseline_data import load_baseline_data
from config import config

# Initialize logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "graph_data" not in st.session_state:
    st.session_state.graph_data = {"nodes": [], "edges": []}
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# @st.cache_resource
# def init_openai():
#     try:
#         return OpenAI(
#             api_key=config.OPENAI_API_KEY,
#             temperature=0.1,
#             max_tokens=400  # Set the max tokens limit here
#         )
#     except Exception as e:
#         st.error(f"Failed to initialize OpenAI: {str(e)}")
#         return None

@st.cache_resource
def init_ollama():
    try:
        return Ollama(
            model="sta_llama3.1_v2",
            num_ctx=6096,
            temperature=0.1,
            base_url="https://0c74-102-91-93-248.ngrok-free.app/",
            callbacks=[StreamingStdOutCallbackHandler()]
        )
    except Exception as e:
        st.error(f"Failed to initialize Ollama: {str(e)}")
        return None

@st.cache_resource
def init_neo4j():
    try:
        return Neo4jGraph(
            url=config.NEO4J_URI,
            username=config.NEO4J_USER,
            password=config.NEO4J_PASSWORD
        )
    except Exception as e:
        st.error(f"Failed to initialize Neo4j: {str(e)}")
        return None

# Initialize components
# openai_llm = init_openai()
ollama_llm = init_ollama()
neo4j_graph = init_neo4j()
neo4j_driver = get_neo4j_driver()
vector_index = create_vector_index()

# if openai_llm is None or neo4j_graph is None or neo4j_driver is None:
#     st.error("Failed to initialize required components. Please check your configurations.")
#     st.stop()

if ollama_llm is None or neo4j_graph is None or neo4j_driver is None:
    st.error("Failed to initialize required components. Please check your configurations.")
    st.stop()

# Create a GraphCypherQAChain
qa_chain = GraphCypherQAChain.from_llm(
    ollama_llm,
    graph=neo4j_graph,
    verbose=True
)

def get_graph_info_for_test_case(test_case_type):
    try:
        with neo4j_driver.session() as session:
            query = f"""
            MATCH (tc:TestCase {{type: '{test_case_type}'}})
            RETURN tc.steps, tc.expectedResults
            """
            result = session.run(query)
            return result.single()
    except Neo4jError as e:
        logger.error(f"Neo4j error occurred: {str(e)}")
        return None


# def generate_test_cases(prompt, test_type, use_knowledge_graph, num_testcases, uploaded_datasets=None):
#     responses = []
#     for i in range(num_testcases):
#         context = ""
        
#         if use_knowledge_graph:
#             similar_testcases = get_similar_testcases(vector_index, prompt)
#             if similar_testcases:
#                 context += "Based on the following similar test cases:\n\n"
#                 for testcase, score in similar_testcases:
#                     context += f"Test Case (similarity score: {score:.2f}):\n{testcase}\n\n"
#             else:
#                 context += "No similar test cases found.\n"
            
#             if uploaded_datasets and i < len(uploaded_datasets):
#                 dataset_info = get_dataset_info(uploaded_datasets[i])
#                 context += f"Using information from dataset: {uploaded_datasets[i].name}\n"
#                 context += f"Dataset info: {dataset_info}\n"
#             else:
#                 graph_info = get_graph_info_for_test_case(test_type)
#                 if graph_info:
#                     steps, expected_results = graph_info
#                     context += f"Steps from graph: {steps}\nExpected Results: {expected_results}\n"
#                 else:
#                     logger.warning("No additional information found in the knowledge graph.")
#                     context += "No additional relevant information found in the knowledge graph.\n"
        
#         full_prompt = f"{context}\nGenerate a new test case named '{test_type}_{i+1}' for: {prompt}\n"
#         full_prompt += "Please follow a similar structure to the example test cases, including all relevant sections (Settings, Variables, Test Cases) and maintain a step-by-step approach."

#         response = ollama_llm(full_prompt)
#         add_prompt_to_graph(neo4j_driver, prompt, response, f"{test_type}_{i+1}")
#         responses.append(response)
    
#     return responses

def generate_test_cases(prompt, test_type, use_knowledge_graph, num_testcases, uploaded_datasets=None):
    responses = []
    for i in range(num_testcases):
        context = ""
        
        if use_knowledge_graph:
            # Fetch only relevant test cases from the knowledge graph, without similarity scores
            graph_info = get_graph_info_for_test_case(test_type)
            if graph_info:
                steps, expected_results = graph_info
                context += f"Steps from graph: {steps}\nExpected Results: {expected_results}\n"
            else:
                logger.warning("No relevant information found in the knowledge graph.")
                context += "No relevant information found in the knowledge graph.\n"
        
        if uploaded_datasets and i < len(uploaded_datasets):
            # Handle information from the uploaded datasets
            dataset_info = get_dataset_info(uploaded_datasets[i])
            context += f"Using information from dataset: {uploaded_datasets[i].name}\n"
            context += f"Dataset info: {dataset_info}\n"
        
        # Construct the final prompt for LLM generation
        full_prompt = f"{context}\nGenerate a new test case named '{test_type}_{i+1}' for: {prompt}\n"
        full_prompt += "Please follow a similar structure to the example test cases, including all relevant sections (Settings, Variables, Test Cases) and maintain a step-by-step approach."

        # Call the LLM model for test case generation
        response = ollama_llm(full_prompt)

        # Append generated response
        responses.append(response)
        
        # Add the response and prompt to the knowledge graph for future reference
        add_prompt_to_graph(neo4j_driver, prompt, response, f"{test_type}_{i+1}")
    
    return responses



def get_dataset_info(dataset):
    # This function would extract relevant information from the dataset
    # For demonstration, we'll just return a simple summary
    try:
        df = pd.read_csv(dataset) if dataset.name.endswith('.csv') else pd.read_excel(dataset)
        return f"Columns: {', '.join(df.columns)}, Rows: {len(df)}"
    except Exception as e:
        return f"Error reading dataset: {str(e)}"

def visualize_graph(nodes, edges):
    G = nx.Graph()
    for node in nodes:
        node_name = str(node['name'])
        G.add_node(node_name, title=node['type'])
    for edge in edges:
        source = str(edge['source'])
        target = str(edge['target'])
        G.add_edge(source, target, title=edge['relation'])

    net = Network(notebook=False, width="100%", height="500px")
    net.from_nx(G)
    net.save_graph("pyvis_graph.html")
    
    with open("pyvis_graph.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    components.html(html, height=500)

# Sidebar
st.sidebar.title("Configuration")
use_knowledge_graph = st.sidebar.checkbox("Use Knowledge Graph", value=True)
test_type = st.sidebar.radio("Select Test Case Type", ["Keyword-Driven", "Data-Driven"])

if st.sidebar.button("Load Baseline Data"):
    baseline_file_path = "combineddata.csv"
    load_baseline_data(baseline_file_path)
    st.sidebar.success("Baseline data loaded successfully!")

uploaded_files = st.sidebar.file_uploader("Upload test case data (CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file not in st.session_state.uploaded_files:
            st.session_state.uploaded_files.append(uploaded_file)
            try:
                data = pd.read_csv(uploaded_file, encoding='ISO-8859-1') if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
                nodes, edges = map_data_to_graph(data)
                update_neo4j_with_graph(neo4j_driver, nodes, edges)
                st.session_state.graph_data["nodes"].extend(nodes)
                st.session_state.graph_data["edges"].extend(edges)
            except Exception as e:
                st.sidebar.error(f"Error processing file {uploaded_file.name}: {str(e)}")
    st.sidebar.success(f"Knowledge graph updated with {len(st.session_state.uploaded_files)} datasets!")

if st.session_state.uploaded_files:
    st.sidebar.subheader("Uploaded Files")
    for file in st.session_state.uploaded_files:
        st.sidebar.text(file.name)

if st.sidebar.button("Clear Session and Database"):
    st.session_state.messages = []
    st.session_state.graph_data = {"nodes": [], "edges": []}
    st.session_state.uploaded_files = []
    clear_neo4j_database(neo4j_driver)
    st.sidebar.success("Session cleared and database emptied!")

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.sidebar.success("Conversation cleared!")

# Visualization in sidebar
if st.session_state.graph_data["nodes"]:
    st.sidebar.subheader("Knowledge Graph Visualization")
    visualize_graph(st.session_state.graph_data["nodes"], st.session_state.graph_data["edges"])
    
    st.sidebar.subheader("Data Summary")
    df_nodes = pd.DataFrame(st.session_state.graph_data["nodes"])
    fig = px.pie(df_nodes, names='type', title='Distribution of Node Types')
    st.sidebar.plotly_chart(fig, use_container_width=True)

# Main content
st.title("sTA-LLaMA3.1 - Software Testing Automation Chatbot")
st.markdown("""
This advanced chatbot assists in generating software test cases using AI and knowledge graph technology. 
It can create both keyword-driven and data-driven test cases based on your inputs and uploaded datasets.
""")

# Chat interface
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input area
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    prompt = st.text_input("Enter your prompt for test case generation:")
with col2:
    test_case_option = st.radio("Generation method:", ["Custom", "Dataset-based"], horizontal=True)
with col3:
    if test_case_option == "Custom":
        num_testcases = st.number_input("Number of test cases:", min_value=1, value=1, step=1)
    else:
        num_testcases = len(st.session_state.uploaded_files)
        st.write(f"Generating {num_testcases} test cases")

if st.button("Generate Test Cases"):
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            uploaded_datasets = st.session_state.uploaded_files if test_case_option == "Dataset-based" else None
            responses = generate_test_cases(prompt, test_type, use_knowledge_graph, num_testcases, uploaded_datasets)
            
            for i, response in enumerate(responses, 1):
                with st.expander(f"Test Case {i}"):
                    st.markdown(response)
                    st.download_button(
                        label=f"Download Test Case {i}",
                        data=response,
                        file_name=f"generated_test_case_{i}.txt",
                        mime="text/plain"
                    )
            
            st.session_state.messages.append({"role": "assistant", "content": "\n\n".join(responses)})
    else:
        st.warning("Please enter a prompt for test case generation.")

# Instructions
st.markdown("""
## How to use this advanced chatbot:
1. Configure the chatbot using the sidebar options.
2. Upload test case datasets to enhance the Knowledge Graph.
3. Enter a prompt and specify the number of test cases to generate.
4. Click 'Generate Test Cases' to create test cases based on your input.
5. View and download the generated test cases.
6. Refer to previous conversations in the chat history.
7. Clear the conversation or reset the entire session as needed.
""")