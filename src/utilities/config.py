from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    NEO4J_URI = os.getenv('NEO4J_URI')
    NEO4J_USER = os.getenv('NEO4J_USER')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    MODEL_ENDPOINT = os.getenv('MODEL_ENDPOINT')

config = Config()
