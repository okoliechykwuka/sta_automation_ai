from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    NEO4J_URI = os.getenv('NEO4J_URI')
    NEO4J_USER = os.getenv('NEO4J_USER')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    MODEL_ENDPOINT = os.getenv('MODEL_ENDPOINT')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app_config = Config()
print(f"Loaded OPENAI_API_KEY: {app_config.OPENAI_API_KEY}")

# print(f"Loaded OPENAI_API_KEY: {config.OPENAI_API_KEY}")
print(f"Loaded MODEL_ENDPOINT: {app_config.MODEL_ENDPOINT}")
