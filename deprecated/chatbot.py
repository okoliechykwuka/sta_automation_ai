import streamlit as st
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
from fast_language_model import FastLanguageModel
import torch
import pprint

# Load the fine-tuned model
model_name = "chukypedro/model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Enable faster inference
FastLanguageModel.for_inference(model)

# Prompt template
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Input:
{input}

### Response:
{output}"""

def generate_test_case(test_type, input_text):
    instruction = f"Generate {test_type} Robot Framework test cases for the following scenario:"
    inputs = tokenizer(
        [
            alpaca_prompt.format(
                instruction=instruction,
                input=f"Test Case Type: {test_type}\nTest Case Name: {input_text}",
                output="",
            )
        ],
        return_tensors="pt"
    ).to("cuda" if torch.cuda.is_available() else "cpu")

    outputs = model.generate(**inputs, max_new_tokens=600, use_cache=True)
    return tokenizer.batch_decode(outputs)[0]

def process_file(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        st.error("Unsupported file format. Please upload a CSV or XLSX file.")
        return None
    return df.to_dict(orient='records')

st.title("Robot Framework Test Case Generator")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

test_type = st.selectbox("Select test case type:", ["Keyword-driven", "Data-driven"])

uploaded_file = st.file_uploader("Upload input file (xlsx, csv)", type=["xlsx", "csv"])

user_input = st.text_input("Enter your test scenario:")

if st.button("Generate Test Case"):
    if user_input or uploaded_file:
        if uploaded_file:
            data = process_file(uploaded_file)
            if data:
                for item in data:
                    test_case = generate_test_case(test_type, str(item))
                    st.session_state.chat_history.append(("User", f"File input: {item}"))
                    st.session_state.chat_history.append(("AI", test_case))
        else:
            test_case = generate_test_case(test_type, user_input)
            st.session_state.chat_history.append(("User", user_input))
            st.session_state.chat_history.append(("AI", test_case))
    else:
        st.warning("Please enter a test scenario or upload a file.")

# Display chat history
st.subheader("Chat History")
for role, message in st.session_state.chat_history:
    if role == "User":
        st.text_input("User:", message, key=f"user_{len(st.session_state.chat_history)}", disabled=True)
    else:
        st.code(message, language="robotframework")

# Option to clear chat history
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.experimental_rerun()