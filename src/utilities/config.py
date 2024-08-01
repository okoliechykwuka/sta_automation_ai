from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    NEO4J_URI = os.getenv('NEO4J_URI')
    NEO4J_USER = os.getenv('NEO4J_USER')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')
    MODEL_ENDPOINT = "https://6407-102-91-4-155.ngrok-free.app/"  # Replace with your actual model endpoint

config = Config()
