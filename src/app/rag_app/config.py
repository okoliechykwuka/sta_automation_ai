from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    NEO4J_URI = os.getenv('NEO4J_URI')
    NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    MODEL_ENDPOINT = "https://4b98-102-91-92-8.ngrok-free.app/"  # Replace with your actual model endpoint

config = Config()