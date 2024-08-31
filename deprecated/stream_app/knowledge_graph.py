import sys
import os
import re
from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable

# Ensure the correct import path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../utilities'))

from config import config

class KnowledgeGraph:
    def __init__(self):
        try:
            self.driver = GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))
        except AuthError as e:
            raise Exception(f"Failed to authenticate with Neo4j: {str(e)}")
        except ServiceUnavailable as e:
            raise Exception(f"Neo4j service is unavailable: {str(e)}")
        except Exception as e:
            raise Exception(f"Failed to connect to Neo4j: {str(e)}")

    def close(self):
        try:
            self.driver.close()
        except Exception as e:
            raise Exception(f"Failed to close Neo4j connection: {str(e)}")

    def create_node(self, label, properties):
        try:
            with self.driver.session() as session:
                result = session.write_transaction(self._create_and_return_node, label, properties)
            return result
        except Exception as e:
            raise Exception(f"Error creating node: {str(e)}")

    @staticmethod
    def _create_and_return_node(tx, label, properties):
        # Sanitize the label
        label = re.sub(r'[^\w\s]', '_', label)

        # Construct the query safely
        query = f"CREATE (n:{label} {{"
        for key, value in properties.items():
            if isinstance(value, str):
                value = value.replace('"', '\\"')  # Escape double quotes if present
                value = f'"{value}"'  # Wrap strings in double quotes
            elif isinstance(value, (int, float, bool)):
                value = str(value)
            else:
                continue  # Skip invalid types
            query += f"{key}: {value}, "
        query = query.rstrip(", ") + "}) RETURN n"
        
        # Run the query
        result = tx.run(query)
        return result.single()[0]
