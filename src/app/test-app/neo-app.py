import streamlit as st
import pandas as pd
from fpdf import FPDF
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms.ollama import Ollama
from rag import setup_rag, query_knowledge_graph

# Set page config
st.set_page_config(page_title="Software Test Automation AI", layout="wide", page_icon="🧪")

ollama_llm = Ollama(model="sta_llama3:latest", num_ctx=6096, temperature=0.1, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
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

# Set up RAG
retriever = setup_rag()

@st.cache_data
def process_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)

def generate_llama_response(prompt, use_rag=True):
    try:
        if use_rag:
            # Query the knowledge graph
            relevant_docs = query_knowledge_graph(retriever, prompt)
            
            # Augment the prompt with relevant information
            augmented_prompt = f"{prompt}\n\nRelevant information:\n"
            for doc in relevant_docs:
                augmented_prompt += f"- {doc.page_content}\n"
        else:
            augmented_prompt = prompt
        
        # Generate response using the augmented prompt
        result = ollama_llm(augmented_prompt, max_tokens=200, temperature=0.7, top_p=0.9)
        return result
    except Exception as e:
        st.error(f"Error generating response with LLaMA: {str(e)}")
        return "Error in generating response."

def export_to_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    return pdf.output(dest="S").encode("latin-1")

# Main layout
st.title('Software Test Automation AI')

# Sidebar
with st.sidebar:
    model_choice = st.selectbox("Choose the model:", ["Llama Custom"])
    test_case_type = st.selectbox("Select test case type:", ["Functional", "Performance", "Keyword-driven", "Security", "Usability", "Data-Driven"])
    use_rag = st.checkbox("Use Knowledge Graph RAG", value=True)
    if model_choice == "Llama Custom":
        temperature = st.slider('Temperature', 0.01, 2.0, 0.7, 0.01)
        top_p = st.slider('Top P', 0.01, 1.0, 0.9, 0.01)

    # Display chat history
    st.subheader("Conversation History")
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        st.text(f"{message['role'].capitalize()}: {message['content']}")

    # Clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.experimental_rerun()

# Main content
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area("Enter your test scenario:", height=150)

with col2:
    uploaded_file = st.file_uploader("Upload CSV or XLSX file for data-driven testing", type=['csv', 'xlsx'])

    if uploaded_file is not None:
        try:
            df = process_uploaded_file(uploaded_file)
            st.write("File uploaded successfully. Preview:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")

if st.button("Generate Test Case", key="generate_button"):
    response = generate_llama_response(user_input, use_rag)
    
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.text_area("Generated Test Case", value=response, height=300)

    # Export to PDF button
    pdf = export_to_pdf(response)
    st.download_button(
        label="Download Test Case as PDF",
        data=pdf,
        file_name="test_case.pdf",
        mime="application/pdf"
    )

if __name__ == "__main__":
    st.sidebar.markdown("## About")
    st.sidebar.info("This is a Software Test Automation AI powered by a custom LLaMA model and a Neo4j knowledge graph.")