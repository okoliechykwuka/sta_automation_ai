from neo4j import GraphDatabase
import networkx as nx
from pyvis.network import Network

class KnowledgeGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_graph(self):
        with self.driver.session() as session:
            session.write_transaction(self._create_and_return_graph)

    @staticmethod
    def _create_and_return_graph(tx):
        query = (
            "CREATE (st:Topic {name: 'Software Testing'})"
            "CREATE (kt:Topic {name: 'Keyword Testing'})"
            "CREATE (ddt:Topic {name: 'Data-Driven Testing'})"
            "CREATE (st)-[:INCLUDES]->(kt)"
            "CREATE (st)-[:INCLUDES]->(ddt)"
            "CREATE (tc:Topic {name: 'Test Cases'})"
            "CREATE (kt)-[:USES]->(tc)"
            "CREATE (ddt)-[:USES]->(tc)"
            "CREATE (td:Topic {name: 'Test Data'})"
            "CREATE (ddt)-[:REQUIRES]->(td)"
            "RETURN st, kt, ddt, tc, td"
        )
        result = tx.run(query)
        return result.single()

    def get_graph(self):
        with self.driver.session() as session:
            return session.read_transaction(self._get_and_return_graph)

    @staticmethod
    def _get_and_return_graph(tx):
        query = (
            "MATCH (n)-[r]->(m) RETURN n.name AS source, type(r) AS type, m.name AS target"
        )
        result = tx.run(query)
        return [(record["source"], record["type"], record["target"]) for record in result]

def create_networkx_graph(neo4j_graph):
    G = nx.Graph()
    for source, rel, target in neo4j_graph:
        G.add_edge(source, target, relationship=rel)
    return G

def visualize_graph(G):
    net = Network(notebook=True, width="100%", height="500px")
    net.from_nx(G)
    net.show("knowledge_graph.html")

if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"

    kg = KnowledgeGraph(uri, user, password)
    kg.create_graph()
    neo4j_graph = kg.get_graph()
    kg.close()

    G = create_networkx_graph(neo4j_graph)
    visualize_graph(G)