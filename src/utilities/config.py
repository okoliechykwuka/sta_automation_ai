from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file
load_dotenv()

try:
    import streamlit as st
    NEO4J_URI = st.secrets.get("NEO4J_URI")
    NEO4J_USER = st.secrets.get("NEO4J_USER")
    NEO4J_PASSWORD = st.secrets.get("NEO4J_PASSWORD")
    MODEL_ENDPOINT = st.secrets.get("MODEL_ENDPOINT")
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")
except (ImportError, FileNotFoundError):
    # If streamlit is not installed or secrets.toml is missing
    NEO4J_URI = None
    NEO4J_USER = None
    NEO4J_PASSWORD = None
    MODEL_ENDPOINT = None
    OPENAI_API_KEY = None

# If any of the variables are None, try to get them from environment variables
if NEO4J_URI is None:
    from dotenv import load_dotenv
    load_dotenv()
    NEO4J_URI = os.getenv('NEO4J_URI')
    NEO4J_USER = os.getenv('NEO4J_USER')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    MODEL_ENDPOINT = os.getenv('MODEL_ENDPOINT')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

class Config:
    NEO4J_URI = NEO4J_URI
    NEO4J_USER = NEO4J_USER
    NEO4J_PASSWORD = NEO4J_PASSWORD
    MODEL_ENDPOINT = MODEL_ENDPOINT
    OPENAI_API_KEY = OPENAI_API_KEY

app_config = Config()

# print(f"Loaded OPENAI_API_KEY: {app_config.OPENAI_API_KEY}")
# print(f"Loaded MODEL_ENDPOINT: {app_config.MODEL_ENDPOINT}")
