from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables from .env file
load_dotenv()

class Config:
    def __init__(self):
        # First, try to get secrets from st.secrets (works on Streamlit Cloud)
        self.NEO4J_URI = st.secrets.get("NEO4J_URI")
        self.NEO4J_USER = st.secrets.get("NEO4J_USER")
        self.NEO4J_PASSWORD = st.secrets.get("NEO4J_PASSWORD")
        self.MODEL_ENDPOINT = st.secrets.get("MODEL_ENDPOINT")
        self.OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")

        # If any are None (e.g., running locally), load from .env
        if not all([self.NEO4J_URI, self.NEO4J_USER, self.NEO4J_PASSWORD, self.MODEL_ENDPOINT, self.OPENAI_API_KEY]):
            load_dotenv()
            self.NEO4J_URI = os.getenv('NEO4J_URI', self.NEO4J_URI)
            self.NEO4J_USER = os.getenv('NEO4J_USER', self.NEO4J_USER)
            self.NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', self.NEO4J_PASSWORD)
            self.MODEL_ENDPOINT = os.getenv('MODEL_ENDPOINT', self.MODEL_ENDPOINT)
            self.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', self.OPENAI_API_KEY)

app_config = Config()

# For debugging, you can print out which variables were loaded
# Be cautious not to print sensitive information like passwords or API keys
st.write(f"Loaded NEO4J_URI: {app_config.NEO4J_URI}")
st.write(f"Loaded MODEL_ENDPOINT: {app_config.MODEL_ENDPOINT}")
