import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import pandas as pd
from fpdf import FPDF
import os

# Set page configuration
st.set_page_config(page_title="Software Test Automation AI", layout="wide", page_icon="🧪")

# Load the model and tokenizer with updated caching method
@st.cache_resource
def load_llama_model():
    try:
        model_directory = "model"  # Adjust this path if needed
        tokenizer = AutoTokenizer.from_pretrained(model_directory)
        model = AutoModelForCausalLM.from_pretrained(model_directory)
        return tokenizer, model
    except Exception as e:
        st.error(f"Error loading the LLaMA model: {str(e)}")
        return None, None

tokenizer, model = load_llama_model()

def generate_llama_response(prompt):
    try:
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(inputs.input_ids, max_length=200, temperature=0.7, top_p=0.9)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        st.error(f"Error generating response with LLaMA: {str(e)}")
        return "Error in generating response."

# Streamlit components
st.title('Software Test Automation AI')

# Ensure the image path is relative to the script or an absolute path
image_path = ".streamlit/robot_head_logo-removebg-preview.png"
if os.path.exists(image_path):
    st.image(image_path, width=100)
else:
    st.error("Image not found, please check the path.")

with st.sidebar:
    model_choice = st.selectbox("Choose the model:", ["Llama Custom", "OpenAI GPT"])
    test_case_type = st.selectbox("Select test case type:", ["Functional", "Performance", "Keyword-driven", "Security", "Usability", "Data-Driven"])

user_input = st.text_area("Enter your test scenario:", height=150)

uploaded_file = st.file_uploader("Upload CSV or XLSX file for data-driven testing", type=['csv', 'xlsx'])
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
        st.write("File uploaded successfully. Preview:")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")

if st.button("Generate Test Case"):
    uploaded_data = df if 'df' in locals() else None
    with st.spinner('Generating response...'):
        response = generate_llama_response(user_input) if model_choice == "Llama Custom" else "Feature not implemented"
        st.success('Done!')
    st.text_area("Generated Test Case", value=response, height=300)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, response)
    
    st.download_button(
        label="Download Test Case as PDF",
        data=pdf.output(dest="S").encode("latin-1"),
        file_name="test_case.pdf",
        mime="application/pdf"
    )