import streamlit as st
import openai
from llama_cpp import Llama
import pandas as pd
from fpdf import FPDF
import io
import base64

st.set_page_config(page_title="Software Test Automation AI", layout="wide", page_icon="🧪")

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

# Load OpenAI API key from secrets
def load_api_key():
    try:
        return st.secrets["OPENAI_API_KEY"]
    except KeyError:
        st.error("Failed to load API key: Check your secrets configuration.")
        return None

api_key = load_api_key()
if api_key:
    openai.api_key = api_key

@st.cache_resource
def load_llama_model():
    try:
        model = Llama(model_path='./robotframeworktest.Q4_K_M.gguf')
        return model
    except Exception as e:
        st.error(f"Error loading the LLaMA model: {str(e)}")
        return None

model = load_llama_model()

def call_openai_model(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a test case generator that precisely follows given examples and instructions."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error calling OpenAI: {str(e)}")
        return "Error in generating response."

def generate_llama_response(prompt):
    try:
        result = model(prompt, max_tokens=200, temperature=0.7, top_p=0.9)
        response = "".join([res['text'] for res in result['choices']])
        return response.strip()
    except Exception as e:
        st.error(f"Error generating response with LLaMA: {str(e)}")
        return "Error in generating response."

@st.cache_data
def process_uploaded_file(uploaded_file):
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    else:
        return pd.read_excel(uploaded_file)

def generate_test_case(model_choice, test_case_type, user_input, uploaded_data=None):
    prompt = f"Generate a {test_case_type} test case for the following scenario:\n{user_input}\n"
    
    if uploaded_data is not None and not uploaded_data.empty:
        prompt += f"\nUse the following data for data-driven robot framework testcase generation:\n{uploaded_data.to_string(index=False)}"
    
    if model_choice == "Llama Custom" and model:
        return generate_llama_response(prompt)
    elif model_choice == "OpenAI GPT":
        return call_openai_model(prompt)
    else:
        return "Please select a model and enter a scenario."

def export_to_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, content)
    return pdf.output(dest="S").encode("latin-1")

# Main layout
st.title('Software Test Automation AI')
st.image('.streamlit/robot_head_logo-removebg-preview.png', width=100)

# Sidebar
with st.sidebar:
    model_choice = st.selectbox("Choose the model:", ["Llama Custom", "OpenAI GPT"])
    test_case_type = st.selectbox("Select test case type:", ["Functional", "Performance", "Keyword-driven", "Security", "Usability", "Data-Driven"])
    if model_choice == "Llama Custom":
        temperature = st.slider('Temperature', 0.01, 2.0, 0.7, 0.01)
        top_p = st.slider('Top P', 0.01, 1.0, 0.9, 0.01)

    # Display chat history
    st.subheader("Conversation History")
    if 'messages' in st.session_state:
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
    uploaded_data = df if 'df' in locals() else None
    response = generate_test_case(model_choice, test_case_type, user_input, uploaded_data)
    
    if 'messages' not in st.session_state:
        st.session_state.messages = []
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
