import streamlit as st
import pandas as pd
from fpdf import FPDF
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms.ollama import Ollama

from kg import KnowledgeGraph
from rag_components import rag_pipeline
from config import config

# Initialize Knowledge Graph
kg = KnowledgeGraph()

# Use the model endpoint from the configuration
model_endpoint = config.MODEL_ENDPOINT

# Function to build the knowledge graph from CSV data
def build_knowledge_graph(df):
    for _, row in df.iterrows():
        kg.create_testcase_node(
            prompt=row['prompt'],
            testcase_type=row['testcase_type'],
            testcase_name=row['testcase_name'],
            documentation=row['documentation'],
            response=row['response']
        )
    st.success("Knowledge Graph built successfully!")

# Function to clear the knowledge graph
def clear_knowledge_graph():
    with kg.driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    st.success("Old Knowledge Graph data cleared successfully!")

def sanitize_for_pdf(text):
    return text.encode('latin-1', 'replace').decode('latin-1')

# Set page config
st.set_page_config(page_title="Software Test Automation AI", layout="wide", page_icon="🧪")

# Initialize Ollama client
@st.cache_resource
def init_ollama():
    try:
        return Ollama(
            model="sta_llama3:latest",
            num_ctx=6096,
            temperature=0.1,
            base_url=model_endpoint,
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
        )
    except Exception as e:
        st.error(f"Failed to initialize Ollama: {str(e)}")
        return None

ollama_llm = init_ollama()

# Custom CSS (unchanged)
st.markdown("""
    <style>
    .stButton>button {
        color: #FFFFFF;
        background-color: #0E76A8;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        background-color: #2D2D2D;
        color: #FFFFFF;
    }
    .stTextArea>div>div>textarea {
        background-color: #2D2D2D;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("Knowledge Graph")
    uploaded_file = st.file_uploader("Upload CSV file for knowledge graph", type=['csv'])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if st.button("Clear Old Data"):
            clear_knowledge_graph()
        if st.button("Build Knowledge Graph"):
            build_knowledge_graph(df)
    
    st.subheader("Model Settings")
    model_choice = st.selectbox("Choose the model:", ["Llama Custom"])
    test_case_type = st.selectbox("Select test case type:", ["Keyword-driven", "Data-Driven"])
    if model_choice == "Llama Custom":
        temperature = st.slider('Temperature', 0.01, 2.0, 0.7, 0.01)
        top_p = st.slider('Top P', 0.01, 1.0, 0.9, 0.01)

    st.subheader("Conversation History")
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.experimental_rerun()

# Main content
st.title('Software Test Automation AI')

col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area("Enter your test scenario:", height=150)

with col2:
    uploaded_file = st.file_uploader("Upload CSV or XLSX file for data-driven testing", type=['csv', 'xlsx'])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
            st.write("File uploaded successfully. Preview:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")

if st.button("Generate Test Case", key="generate_button"):
    uploaded_data = df if 'df' in locals() else None
    response = rag_pipeline(user_input, kg, model_endpoint, test_case_type, uploaded_data)
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.text_area("Generated Test Case", value=response, height=300)

    # Export to PDF button
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    sanitized_response = sanitize_for_pdf(response)
    pdf.multi_cell(0, 10, sanitized_response)
    pdf_output = pdf.output(dest="S").encode("latin-1")
    st.download_button(
        label="Download Test Case as PDF",
        data=pdf_output,
        file_name="test_case.pdf",
        mime="application/pdf"
    )

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Close the KG connection when the app is done
kg.close()