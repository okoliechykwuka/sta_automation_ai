import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
from streamlit_pyvis import st_pyvis
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from neo4j import GraphDatabase
import plotly.express as px
import streamlit.components.v1 as components

# Initialize Streamlit app
st.set_page_config(layout="wide")
st.title("Advanced Gemini Pro - ChatBot with Multiple Data Upload")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "graph_data" not in st.session_state:
    st.session_state.graph_data = {"nodes": [], "edges": []}
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []

# Caching for database interactions
@st.cache_resource
def init_ollama():
    try:
        return Ollama(
            model="sta_llama3.1_v2",
            num_ctx=6096,
            temperature=0.1,
            base_url="https://18b8-197-210-76-25.ngrok-free.app/",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
        )
    except Exception as e:
        st.error(f"Failed to initialize Ollama: {str(e)}")
        return None

@st.cache_resource
def init_neo4j():
    try:
        return Neo4jGraph(
            url="neo4j+s://your-neo4j-url.databases.neo4j.io",
            username="neo4j",
            password="your-password"
        )
    except Exception as e:
        st.error(f"Failed to initialize Neo4j: {str(e)}")
        return None

# Initialize Ollama and Neo4j
ollama_llm = init_ollama()
neo4j_graph = init_neo4j()

if ollama_llm is None or neo4j_graph is None:
    st.error("Failed to initialize required components. Please check your configurations.")
    st.stop()

# Create a GraphCypherQAChain
qa_chain = GraphCypherQAChain.from_llm(
    ollama_llm,
    graph=neo4j_graph,
    verbose=True
)

# Function to map data to Neo4j graph schema
def map_data_to_graph(data):
    nodes = []
    edges = []
    for index, row in data.iterrows():
        testcase_node = {
            "name": row['TestCase'], 
            "type": row['TestType']
        }
        nodes.append(testcase_node)
        
        if 'KeywordName' in row and pd.notna(row['KeywordName']):
            keyword_node = {"name": row['KeywordName'], "type": "Keyword"}
            nodes.append(keyword_node)
            edges.append({
                "source": row['TestCase'], 
                "target": row['KeywordName'], 
                "relation": "USES_KEYWORD"
            })
        
        if 'Arguments' in row and pd.notna(row['Arguments']):
            argument_node = {"name": row['Arguments'], "type": "Argument"}
            nodes.append(argument_node)
            edges.append({
                "source": row['KeywordName'], 
                "target": row['Arguments'], 
                "relation": "HAS_ARGUMENT"
            })

        if 'RelatedTestCase' in row and pd.notna(row['RelatedTestCase']):
            edges.append({
                "source": row['TestCase'], 
                "target": row['RelatedTestCase'], 
                "relation": "RELATED_TO"
            })
    
    return nodes, edges

# Function to update Neo4j with mapped nodes and edges
@st.cache_data
def update_neo4j_with_graph(nodes, edges, neo4j_graph):
    driver = GraphDatabase.driver(neo4j_graph.url, auth=(neo4j_graph.username, neo4j_graph.password))
    with driver.session() as session:
        for node in nodes:
            session.run(
                """
                MERGE (n {name: $name, type: $type})
                """, name=node['name'], type=node['type']
            )
        
        for edge in edges:
            session.run(
                """
                MATCH (a {name: $source}), (b {name: $target})
                MERGE (a)-[r:%s]->(b)
                """ % edge['relation'], source=edge['source'], target=edge['target']
            )
    driver.close()

def clear_neo4j_database(neo4j_graph):
    driver = GraphDatabase.driver(neo4j_graph.url, auth=(neo4j_graph.username, neo4j_graph.password))
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    driver.close()

# Function to generate test case based on user input
def generate_test_case(prompt, test_type, use_knowledge_graph):
    if use_knowledge_graph:
        response = qa_chain.run(f"{test_type} test case: {prompt}")
    else:
        response = ollama_llm(f"Generate a {test_type} test case for: {prompt}")
    return response

# Function to visualize the graph
def visualize_graph(nodes, edges):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node['name'], title=node['type'])
    for edge in edges:
        G.add_edge(edge['source'], edge['target'], title=edge['relation'])
    
    net = Network(notebook=True, width="100%", height="500px")
    net.from_nx(G)
    return net.generate_html()

# Sidebar for configuration
st.sidebar.header("Configuration")
use_knowledge_graph = st.sidebar.checkbox("Use Knowledge Graph", value=True)
test_type = st.sidebar.radio("Select Test Case Type", ["Keyword-Driven", "Data-Driven"])

# Multiple file uploader for test case data
uploaded_files = st.sidebar.file_uploader("Upload test case data (CSV or Excel)", type=["csv", "xlsx"], accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file not in st.session_state.uploaded_files:
            st.session_state.uploaded_files.append(uploaded_file)
            data = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            nodes, edges = map_data_to_graph(data)
            update_neo4j_with_graph(nodes, edges, neo4j_graph)
            st.session_state.graph_data["nodes"].extend(nodes)
            st.session_state.graph_data["edges"].extend(edges)
    st.sidebar.success(f"Knowledge graph updated with {len(st.session_state.uploaded_files)} datasets!")

# Display uploaded files
if st.session_state.uploaded_files:
    st.sidebar.subheader("Uploaded Files")
    for file in st.session_state.uploaded_files:
        st.sidebar.text(file.name)

# Search and Filter Options
st.sidebar.header("Search and Filter")
search_query = st.sidebar.text_input("Search for test cases, keywords, or arguments")
filter_type = st.sidebar.multiselect("Filter by type", ["TestCase", "Keyword", "Argument"])

# Interactive Graph Editing
st.sidebar.header("Add Node or Edge")
new_node_name = st.sidebar.text_input("New Node Name")
new_node_type = st.sidebar.selectbox("New Node Type", ["TestCase", "Keyword", "Argument"])
if st.sidebar.button("Add Node"):
    st.session_state.graph_data["nodes"].append({"name": new_node_name, "type": new_node_type})
    update_neo4j_with_graph([{"name": new_node_name, "type": new_node_type}], [], neo4j_graph)

new_edge_source = st.sidebar.selectbox("Edge Source", [node["name"] for node in st.session_state.graph_data["nodes"]])
new_edge_target = st.sidebar.selectbox("Edge Target", [node["name"] for node in st.session_state.graph_data["nodes"]])
new_edge_relation = st.sidebar.text_input("Edge Relation")
if st.sidebar.button("Add Edge"):
    st.session_state.graph_data["edges"].append({"source": new_edge_source, "target": new_edge_target, "relation": new_edge_relation})
    update_neo4j_with_graph([], [{"source": new_edge_source, "target": new_edge_target, "relation": new_edge_relation}], neo4j_graph)

# Main content area
col1, col2 = st.columns([2, 1])


with col1:
    st.header("Chat Interface")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about software testing automation or request a test case..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = generate_test_case(prompt, test_type, use_knowledge_graph)
            st.markdown(response)
            # Add download button for the response
            st.download_button(
                label="Download Test Case",
                data=response,
                file_name="generated_test_case.txt",
                mime="text/plain"
            )
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Multiple test case generation
    st.subheader("Generate Multiple Test Cases")
    num_testcases = st.number_input("Number of test cases to generate", min_value=1, max_value=10, value=3)
    if st.button("Generate Test Cases"):
        all_responses = []
        for i in range(num_testcases):
            response = generate_test_case(f"{prompt} (Variation {i+1})", test_type, use_knowledge_graph)
            st.markdown(f"Test Case {i + 1}:")
            st.code(response)
            all_responses.append(f"Test Case {i + 1}:\n{response}\n\n")
        
        # Add download button for all generated test cases
        combined_responses = "\n".join(all_responses)
        st.download_button(
            label="Download All Test Cases",
            data=combined_responses,
            file_name="all_generated_test_cases.txt",
            mime="text/plain"
        )

with col2:
    st.header("Knowledge Graph Visualization")
    if st.session_state.graph_data["nodes"]:
        graph_html = visualize_graph(st.session_state.graph_data["nodes"], st.session_state.graph_data["edges"])
        components.html(graph_html, height=600)
    else:
        st.info("Upload data or add nodes/edges to visualize the knowledge graph.")

    # Data Visualization
    st.subheader("Data Summary")
    if st.session_state.graph_data["nodes"]:
        df_nodes = pd.DataFrame(st.session_state.graph_data["nodes"])
        fig = px.pie(df_nodes, names='type', title='Distribution of Node Types')
        st.plotly_chart(fig)

# Clear session and database
if st.button("Clear Session and Database"):
    st.session_state.messages = []
    st.session_state.graph_data = {"nodes": [], "edges": []}
    st.session_state.uploaded_files = []
    clear_neo4j_database(neo4j_graph)
    st.success("Session cleared and database emptied!")

# Instructions for users
st.markdown("""
## How to use this advanced chatbot:
1. Configure the chatbot using the sidebar options.
2. Upload multiple test case datasets to enhance the Knowledge Graph.
3. Use the chat interface to generate test cases or ask questions.
4. Visualize and interact with the combined Knowledge Graph from all uploaded datasets.
5. Add new nodes and edges to the graph manually.
6. Generate multiple test cases at once, incorporating data from all uploaded files.
7. Use the search and filter options to explore the combined data.
8. Clear the session and database when you want to start fresh with new data.
""")