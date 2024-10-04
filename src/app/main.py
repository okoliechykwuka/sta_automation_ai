import sys
import os
import streamlit as st
st.cache_resource.clear()
import pandas as pd
import networkx as nx
from pyvis.network import Network
# from langchain_community.llms import Ollama
# from langchain.llms import Ollama
# from langchain.callbacks.manager import Callbackllmsr
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
import plotly.express as px
import streamlit.components.v1 as components
# from langchain_llms import OpenAI
from langchain_community.llms.openai import OpenAI
import logging
from neo4j.exceptions import Neo4jError
from fpdf import FPDF

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, '..'))

from kgraph_index import (
    get_neo4j_driver, create_vector_index, compute_embeddings_for_new_nodes,
    map_data_to_graph, update_neo4j_with_graph, clear_neo4j_database,
    add_prompt_to_graph, get_similar_testcases, get_test_case_structure
)

from baseline_data import load_baseline_data
from utilities.config import app_config
from custom_llm import CloudLLM

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

@st.cache_resource
def init_ollama():
    if not app_config.MODEL_ENDPOINT:
        st.error("MODEL_ENDPOINT is missing.")
        return None
    try:
        
        return CloudLLM(
                endpoint_url=app_config.MODEL_ENDPOINT,
                model="testforceai/sta_llama3.1",
                callbacks=[StreamingStdOutCallbackHandler()]
                
            )
        # return Ollama(
        #     model="sta_llama3.1_v2",
        #     num_ctx=6096,
        #     temperature=0.1,
        #     base_url=app_config.MODEL_ENDPOINT,
        #     callbacks=[StreamingStdOutCallbackHandler()]
        # )
    except Exception as e:
        st.error(f"Failed to initialize Ollama: {str(e)}")
        return None

@st.cache_resource
def init_neo4j():
    if not all([app_config.NEO4J_URI, app_config.NEO4J_USER, app_config.NEO4J_PASSWORD]):
        st.error("Neo4j configuration variables are missing.")
        return None
    try:
        graph = Neo4jGraph(
            url=app_config.NEO4J_URI,
            username=app_config.NEO4J_USER,
            password=app_config.NEO4J_PASSWORD
        )
        # Test the connection
        graph.query("RETURN 1")
        return graph
    except Exception as e:
        st.error(f"Failed to initialize Neo4j: {str(e)}")
        return None

@st.cache_resource
def init_vector_index():
    return create_vector_index()

# Initialize components
ollama_llm = init_ollama()
neo4j_graph = init_neo4j()
neo4j_driver = get_neo4j_driver()
vector_index = init_vector_index()

# Check that all components are initialized
# if not all([ollama_llm, neo4j_graph, neo4j_driver, vector_index]):
#     st.error("Failed to initialize required components. Please check your configurations.")
#     st.stop()
if ollama_llm is None or neo4j_graph is None or neo4j_driver is None or vector_index is None:
    st.error("Failed to initialize required components. Please check your configurations.")
    st.stop()

# if vector_index is None:
#     st.error("Vector index could not be created. Please check your configuration and OpenAI API usage.")
#     st.stop()

# Create a GraphCypherQAChain
qa_chain = GraphCypherQAChain.from_llm(
    ollama_llm,
    graph=neo4j_graph,
    verbose=True,
    allow_dangerous_requests=True
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

def generate_test_cases(prompt, test_type, use_knowledge_graph, num_testcases, uploaded_datasets=None):
    responses = []
    
    for i in range(num_testcases):
        # Display progress for each test case being generated
        st.write(f"Generating test case {i+1}...")
        
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

        response = ollama_llm.invoke(full_prompt)
        responses.append(response)
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

# def download_test_cases(test_cases):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=10)

#     for idx, test_case in enumerate(test_cases, 1):
#         if idx > 1:
#             # line of dashes before each test case (except the first one)
#             pdf.cell(0, 5, "-" * 150, ln=True, align="C")
#             pdf.ln(5)  # space after the line of dashes

#         pdf.cell(200, 8, f"Test Case {idx}", ln=True, align="L")
#         pdf.multi_cell(0, 6, test_case)
#         pdf.ln(5)  # space after each test case
    
#     pdf_output = pdf.output(dest='S').encode('latin1')
#     st.download_button(
#         label="Download Test Cases",
#         data=pdf_output,
#         file_name="generated_test_cases.pdf",
#         mime="application/pdf"
#     )

def download_test_cases(test_cases):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for idx, test_case in enumerate(test_cases, 1):
        if idx > 1:
            pdf.add_page()  # Start each test case on a new page

        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, f"Test Case {idx}", ln=True, align="L")
        pdf.set_font("Arial", size=10)
        
        lines = test_case.split('\n')
        for line in lines:
            if line.startswith('***'):
                pdf.set_font("Arial", 'B', 11)
                pdf.cell(0, 6, line, ln=True)
                pdf.set_font("Arial", size=10)
            else:
                pdf.multi_cell(0, 5, line)
    
    pdf_output = pdf.output(dest='S').encode('latin1')
    st.download_button(
        label="Download Test Cases",
        data=pdf_output,
        file_name="generated_test_cases.pdf",
        mime="application/pdf"
    )

# Sidebar
st.sidebar.title("Configuration")
use_knowledge_graph = st.sidebar.checkbox("Use Knowledge Graph", value=True)
test_type = st.sidebar.radio("Select Test Case Type", ["Keyword-Driven", "Data-Driven"])

if st.sidebar.button("Load Baseline Data"):
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the baseline_file_path
    baseline_file_path = os.path.join(current_dir, "combineddata.csv")
    # baseline_file_path = "combineddata.csv"
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
                # Compute embeddings for new nodes and update vector index
                compute_embeddings_for_new_nodes()
                vector_index = init_vector_index()
                # similar_testcases = get_similar_testcases(vector_index, prompt)
            except Exception as e:
                st.sidebar.error(f"Error processing file {uploaded_file.name}: {str(e)}")
    st.sidebar.success(f"Knowledge graph updated with {len(st.session_state.uploaded_files)} datasets!")

st.sidebar.title("Configuration")
st.sidebar.markdown("""
How to use this advanced chatbot:

1. Enter your prompt for test case generation in the text area.
2. Click the "Generate Test Cases" button to generate the test cases.
3. Review the generated test cases in the text area.
4. If you're satisfied, click the "Download Test Cases" button to download the test cases as a PDF.
5. You can continue the conversation by entering a new prompt in the text area.
""")

if st.sidebar.button("Clear Session and Database"):
    st.session_state.messages = []
    st.session_state.graph_data = {"nodes": [], "edges": []}
    st.session_state.uploaded_files = []
    clear_neo4j_database(neo4j_driver)
    st.sidebar.success("Session cleared and database emptied!")

if st.sidebar.button("Clear Conversation"):
    st.session_state.messages = []
    st.sidebar.success("Conversation cleared!")

# Main content
st.title("STA-LLaMA3.1 - Software Testing Automation Chatbot")

# Input and conversation box
col1, col2 = st.columns([3, 1])
with col1:
    prompt = st.text_input("Enter your prompt for test case generation:")
with col2:
    num_testcases = st.number_input("Number of test cases:", min_value=1, value=1, step=1)

# Display past messages and responses
if "messages" in st.session_state:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Button to generate test cases and continue the conversation
if st.button("Generate Test Cases"):
    if prompt:
        # Store the user's prompt
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display responses
        with st.chat_message("assistant"):
            responses = generate_test_cases(prompt, test_type, use_knowledge_graph, num_testcases)

            # Display each test case in a properly structured format
            formatted_responses = []
            for i, response in enumerate(responses, 1):
                # Split the response into sections
                sections = response.split('***')
                formatted_response = f"Test Case {i}\n"
                for section in sections:
                    if section.strip():
                        # Add section title
                        title = section.split('\n')[0].strip()
                        formatted_response += f"\n*** {title} ***\n"
                        # Add section content with indentation
                        content = '\n'.join(section.split('\n')[1:])
                        formatted_response += '\n'.join([f"    {line}" for line in content.split('\n') if line.strip()])
                        formatted_response += '\n'
                
                st.text_area(f"Test Case {i}", formatted_response, height=300)
                formatted_responses.append(formatted_response)
                
            # Append assistant's responses to messages for continued conversation
            st.session_state.messages.append({"role": "assistant", "content": "\n\n".join(formatted_responses)})
            
            # Allow downloading of the test cases
            download_test_cases(formatted_responses)
    else:
        st.warning("Please enter a prompt for test case generation.")
