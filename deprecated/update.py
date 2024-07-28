import streamlit as st
import openai
from llama_cpp import Llama

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
        # Load the LLaMA model using llama_cpp
        model = Llama(model_path='./unsloth.Q4_K_M.gguf')
        return model
    except Exception as e:
        st.error(f"Error loading the LLaMA model: {str(e)}")
        return None

model = load_llama_model()

# Function to call OpenAI GPT model
def call_openai_model(prompt):
    try:
        response = openai.chat.completions.create(
            engine="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        st.error(f"Error calling OpenAI: {str(e)}")
        return "Error in generating response."

# Function to generate response using LLaMA model
def generate_llama_response(prompt):
    try:
        result = model(prompt, max_tokens=200, temperature=0.7, top_p=0.9)
        response = "".join([res['text'] for res in result['choices']])
        return response.strip()
    except Exception as e:
        st.error(f"Error generating response with LLaMA: {str(e)}")
        return "Error in generating response."

# Streamlit UI
st.title('Chatbot with Model Selection')

with st.sidebar:
    model_choice = st.selectbox("Choose the model:", ["Llama Custom", "OpenAI GPT"])
    if model_choice == "Llama Custom":
        temperature = st.slider('Temperature', 0.01, 2.0, 0.7, 0.01)
        top_p = st.slider('Top P', 0.01, 1.0, 0.9, 0.01)

# User input
user_input = st.text_input("Enter your test scenario:")
if st.button("Generate"):
    if model_choice == "Llama Custom" and model:
        response = generate_llama_response(user_input)
    elif model_choice == "OpenAI GPT":
        response = call_openai_model(user_input)
    else:
        response = "Please select a model and enter a scenario."

    if 'messages' not in st.session_state:
        st.session_state.messages = []
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.text_area("Generated Test Case", value=response, height=300)

# Display chat history
if 'messages' in st.session_state:
    for message in st.session_state.messages:
        st.text(f"{message['role']}: {message['content']}")
