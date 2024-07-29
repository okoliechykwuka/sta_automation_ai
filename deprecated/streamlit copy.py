import streamlit as st
from llama_cpp import Llama  # Hypothetical library supporting gguf

# App title and configuration
st.set_page_config(page_title="Chatbot with GGUF Model")

# Function to load the model
@st.cache_resource()
def load_model(temperature, top_p):
    try:
        model = Llama(
            model_path='./unsloth.Q4_K_M.gguf',
            temperature=temperature,
            top_p=top_p
        )
        return model
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

# Sidebar configuration
with st.sidebar:
    st.title('Chatbot Configuration')
    temperature = st.slider('Temperature', min_value=0.01, max_value=2.0, value=0.7, step=0.01)
    top_p = st.slider('Top P', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    model = load_model(temperature, top_p)
    test_type = st.selectbox("Select test case type:", ["Keyword-driven", "Data-driven"])

# Chat history management
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function to clear chat history
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Chat cleared! How can I assist you now?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating responses
def generate_response(user_input, test_type):
    prompt_format = f"You are a helpful assistant that generates {test_type} Robot Framework testcases. Please generate a testcase for: {user_input}"
    response = model(f"{prompt_format}")  # Adjust how the model is called based on actual API
    return response

# Input and response handling
user_input = st.text_input("Describe the test scenario you want to generate:")
if st.button("Generate Test Case"):
    response = generate_response(user_input, test_type)
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
