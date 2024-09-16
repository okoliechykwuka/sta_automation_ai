from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    NEO4J_URI = st.secrets.get("NEO4J_URI") or os.getenv('NEO4J_URI')
    NEO4J_USER = st.secrets.get("NEO4J_USER") or os.getenv('NEO4J_USER')
    NEO4J_PASSWORD = st.secrets.get("NEO4J_PASSWORD") or os.getenv('NEO4J_PASSWORD')
    MODEL_ENDPOINT = st.secrets.get("MODEL_ENDPOINT") or os.getenv('MODEL_ENDPOINT')
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY") or os.getenv('OPENAI_API_KEY')

app_config = Config()

# print(f"Loaded OPENAI_API_KEY: {app_config.OPENAI_API_KEY}")
# print(f"Loaded MODEL_ENDPOINT: {app_config.MODEL_ENDPOINT}")
