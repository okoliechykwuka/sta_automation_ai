from neo4j import GraphDatabase
from config import config

class KnowledgeGraph:
    def __init__(self):
        self.driver = GraphDatabase.driver(config.NEO4J_URI, auth=(config.NEO4J_USERNAME, config.NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def create_testcase_node(self, prompt, testcase_type, testcase_name, documentation, response):
        with self.driver.session() as session:
            session.write_transaction(self._create_testcase_node, prompt, testcase_type, testcase_name, documentation, response)

    @staticmethod
    def _create_testcase_node(tx, prompt, testcase_type, testcase_name, documentation, response):
        query = (
            "MERGE (t:TestCase {name: $testcase_name}) "
            "SET t.type = $testcase_type, t.documentation = $documentation, t.response = $response "
            "MERGE (p:Prompt {text: $prompt}) "
            "MERGE (t)-[:HAS_PROMPT]->(p)"
        )
        tx.run(query, prompt=prompt, testcase_type=testcase_type, testcase_name=testcase_name, documentation=documentation, response=response)

    def query_graph(self, keyword):
        with self.driver.session() as session:
            return session.read_transaction(self._query_graph, keyword)

    @staticmethod
    def _query_graph(tx, keyword):
        query = (
            "MATCH (t:TestCase)-[:HAS_PROMPT]->(p:Prompt) "
            "WHERE t.name CONTAINS $keyword OR t.type CONTAINS $keyword OR p.text CONTAINS $keyword "
            "RETURN t.name AS testcase_name, t.type AS testcase_type, t.documentation AS documentation, t.response AS response, p.text AS prompt"
        )
        result = tx.run(query, keyword=keyword)
        return [record for record in result]