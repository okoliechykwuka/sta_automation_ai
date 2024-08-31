import sys
import re
import os
import streamlit as st
import pandas as pd
from fpdf import FPDF
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms.ollama import Ollama
# import openai # newly added for openai
# from openai import OpenAI # newly added for openai

# Ensure the correct import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
sys.path.append(os.path.join(current_dir, '../utilities'))

from knowledge_graph import KnowledgeGraph
from rag import rag_pipeline
from config import config

# Initialize Knowledge Graph
kg = KnowledgeGraph()

# Use the model endpoint from the configuration
# model_endpoint = config.MODEL_ENDPOINT # used for ngrok endpoint

# Function to sanitize the input
def sanitize_input(value):
    if isinstance(value, str):
        value = value.strip()
        # Escape single quotes by doubling them for Cypher compatibility
        value = value.replace("'", "''")
        # Avoid using re.sub, as it might remove essential characters; instead, replace problematic characters
        value = value.replace('"', '\\"')  # Escape double quotes
        value = value.replace('\\', '\\\\')  # Escape backslash es
    return value


# Function to build the knowledge graph
def build_knowledge_graph(df):
    if df is not None and not df.empty:
        try:
            # Sanitize the dataframe before using it
            df_sanitized = df.apply(sanitize_input)
            
            for _, row in df_sanitized.iterrows():
                label = sanitize_input(row.iloc[0])  # Assuming the first column is the label
                properties = {sanitize_input(k): sanitize_input(v) for k, v in row.iloc[1:].to_dict().items()}
                kg.create_node(label, properties)
            st.success("Knowledge Graph built successfully!")
        except Exception as e:
            st.error(f"Error building Knowledge Graph: {str(e)}")
    else:
        st.warning("Please upload data before building the Knowledge Graph.")

# Set page config
st.set_page_config(page_title="Software Test Automation AI", layout="wide", page_icon="🧪")

# initialize openai client
# @st.cache_resource
# def init_openai(): # newly added for openai
#     try:
#         return OpenAI(api_key=config.OPENAI_API_KEY)
#     except Exception as e:
#         st.error(f"Failed to initialize OpenAI: {str(e)}")
#         return None

# openai_client = init_openai()


# Initialize Ollama client
@st.cache_resource
def init_ollama():
    try:
        return Ollama(
            model="sta_llama3.1_v2",
            num_ctx=6096,
            temperature=0.1,
            base_url="https://18b8-197-210-76-25.ngrok-free.app/",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
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

# def generate_gpt4_response(prompt): # newly added for openai
#     if openai_client is None:
#         return "OpenAI client is not initialized. Please check your API key or connection and retry."
#     try:
#         response = openai_client.chat.completions.create(
#             model="gpt-4",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7,
#             max_tokens=1000
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         st.error(f"Error generating response with GPT4: {str(e)}")
#         return "Error in generating response."

def generate_llama_response(prompt):
    if ollama_llm is None:
        return "Ollama LLM is not initialized. Please check your connection and retry."
    try:
        result = ollama_llm(prompt)
        return result.strip()
    except Exception as e:
        st.error(f"Error generating response with LLaMA: {str(e)}")
        return "Error in generating response."

@st.cache_data
def process_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)

# testcase generation function for openai
# def generate_test_case(model_choice, test_case_type, user_input, uploaded_data=None): # newly added for openai
#     prompt = f"Generate a {test_case_type} test case for the following scenario:\n{user_input}\n"

#     if uploaded_data is not None and not uploaded_data.empty:
#         prompt += f"\nUse the following data for data-driven robot framework testcase generation:\n{uploaded_data.to_string(index=False)}"

#     return rag_pipeline(prompt, kg, openai_client)   

# testcase generation function for ollama
# Modify the generate_test_case function
def generate_test_case(test_case_type, user_input, uploaded_data=None):
    prompt = f"Generate a {test_case_type} test case for the following scenario:\n{user_input}\n"
    
    if uploaded_data is not None and not uploaded_data.empty:
        prompt += f"\nUse the following data for data-driven robot framework testcase generation:\n{uploaded_data.to_string(index=False)}"
    
    return rag_pipeline(prompt, kg, ollama_llm)


def export_to_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    return pdf.output(dest="S").encode("latin-1")

# Main layout
st.title('Software Test Automation AI')

# Sidebar
# Sidebar layout for file upload and knowledge graph building
with st.sidebar:
    uploaded_file = st.file_uploader("Upload CSV or XLSX file for data-driven testing", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            df = process_uploaded_file(uploaded_file)
            st.session_state.uploaded_data = df  # Store the DataFrame in the session state
            st.write("File uploaded successfully. Preview:")
            st.dataframe(df.head())
            
            if st.button("Build Knowledge Graph"):
                build_knowledge_graph(st.session_state.uploaded_data)
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
    else:
        st.session_state.uploaded_data = None

    model_choice = st.selectbox("Choose the model:", ["Llama Custom"])
    test_case_type = st.selectbox("Select test case type:", ["Keyword-driven", "Data-Driven"])
    if model_choice == "Llama Custom":
        temperature = st.slider('Temperature', 0.01, 2.0, 0.7, 0.01)
        top_p = st.slider('Top P', 0.01, 1.0, 0.9, 0.01)

    # Display chat history
    st.subheader("Conversation History")
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Clear conversation button
    # if st.button("Clear Conversation"):
    #     st.session_state.messages = []
    #     st.experimental_rerun()

# User input area
user_input = st.text_area("Enter your test scenario or prompt:", height=150)

# Main content
# Modify the generate_test_case function call:
if st.button("Generate Test Case", key="generate_button"):
    uploaded_data = st.session_state.uploaded_data if 'uploaded_data' in st.session_state else None
    try:
        response = generate_test_case(test_case_type, user_input, uploaded_data)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.text_area("Generated Test Case", value=response, height=300)
    except Exception as e:
        st.error(f"Error generating test case: {str(e)}")

    # Export to PDF button
    pdf = export_to_pdf(response)
    st.download_button(
        label="Download Test Case as PDF",
        data=pdf,
        file_name="test_case.pdf",
        mime="application/pdf"
    )