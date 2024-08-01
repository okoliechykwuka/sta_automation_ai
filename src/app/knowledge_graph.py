import sys
import os
from neo4j import GraphDatabase

# Ensure the correct import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../utilities'))

from config import config

class KnowledgeGraph:
    def __init__(self):
        self.driver = GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def create_node(self, label, properties):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_node, label, properties)

    @staticmethod
    def _create_and_return_node(tx, label, properties):
        query = f"CREATE (n:{label} {{"
        for key, value in properties.items():
            query += f"{key}: '{value}',"
        query = query[:-1] + "}) RETURN n"
        result = tx.run(query)
        return result.single()[0]
