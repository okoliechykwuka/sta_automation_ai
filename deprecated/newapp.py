import streamlit as st
import requests
import pandas as pd

# Set the title for your application
st.title("Software Test Automation AI")

if 'history' not in st.session_state:
    st.session_state.history = []

test_type = st.selectbox("Select test case type:", ["Keyword-driven", "Data-driven"])
uploaded_file = st.file_uploader("Upload input file (xlsx, csv)", type=["xlsx", "csv"])
user_input = st.text_input("Enter your test scenario:")

def generate_test_case(test_type, input_text):
    response = requests.post('http://localhost:8000/generate', json={
        'test_type': test_type, 
        'input_text': input_text
    })
    if response.status_code == 200:
        return response.json()['generated_text']
    else:
        return "Failed to generate test case due to an error."

def process_file(file, test_type):
    if file.type == "csv":
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    results = []
    for index, row in df.iterrows():
        input_text = " ".join(row.astype(str))
        result = generate_test_case(test_type, input_text)
        results.append(result)
    return "\n".join(results)

if st.button("Generate Test Case"):
    if user_input:
        test_case = generate_test_case(test_type, user_input)
        st.session_state.history.append((user_input, test_case))
        st.code(test_case, language="robotframework")
    elif uploaded_file:
        test_case = process_file(uploaded_file, test_type)
        st.session_state.history.append(("File: " + uploaded_file.name, test_case))
        st.code(test_case, language="robotframework")
    else:
        st.warning("Please enter a test scenario or upload a file.")

if st.session_state.history:
    st.header("Session History")
    for i, (inp, res) in enumerate(st.session_state.history):
        st.subheader(f"Session {i+1}")
        st.text_area("Query", value=inp, height=100, key=f"query{i}")
        st.text_area("Generated Test Case", value=res, height=300, key=f"response{i}")