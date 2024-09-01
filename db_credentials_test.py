# from neo4j import GraphDatabase

# uri = "neo4j+s://155b6ca5.databases.neo4j.io"
# user = "neo4j"
# password = "8nQ9YiUMHtaUFLPjswnKAHDgW0kulDz6jcnPlM8ofGk"

# try:
#     driver = GraphDatabase.driver(uri, auth=(user, password))
#     with driver.session() as session:
#         result = session.run("MATCH (n) RETURN count(n) AS count")
#         record = result.single()
#         print(f"Number of nodes in the database: {record['count']}")
#     driver.close()
# except Exception as e:
#     print(f"Failed to connect to Neo4j: {str(e)}")


import requests
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_ENDPOINT = os.getenv('MODEL_ENDPOINT')

response = requests.post(f"{MODEL_ENDPOINT}/api/generate", json={
    "model": "sta_llama3.1_v2",
    "prompt": "Hello, world!"
})

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")