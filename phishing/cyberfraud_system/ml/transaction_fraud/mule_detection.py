"""
Graph-Based Mule Detection Module
Detect suspicious clusters in transaction graphs.
"""
import networkx as nx

def build_transaction_graph(transactions):
    """
    Build a directed transaction graph.

    Args:
        transactions (list): List of transactions, where each transaction is a tuple (sender, receiver, amount).

    Returns:
        nx.DiGraph: Directed transaction graph.
    """
    graph = nx.DiGraph()
    for sender, receiver, amount in transactions:
        graph.add_edge(sender, receiver, weight=amount)
    return graph

def detect_suspicious_clusters(graph):
    """
    Detect suspicious clusters in the transaction graph.

    Args:
        graph (nx.DiGraph): Directed transaction graph.

    Returns:
        list: List of suspicious clusters with details.
    """
    suspicious_clusters = []

    # Detect cyclic transactions
    cycles = list(nx.simple_cycles(graph))
    for cycle in cycles:
        suspicious_clusters.append({
            "type": "cyclic_transaction",
            "accounts": cycle,
            "risk_level": "HIGH"
        })

    # Detect high fan-in / fan-out nodes
    for node in graph.nodes:
        in_degree = graph.in_degree(node)
        out_degree = graph.out_degree(node)
        if in_degree > 5 or out_degree > 5:
            suspicious_clusters.append({
                "type": "high_fan_in_out",
                "account": node,
                "risk_level": "MEDIUM"
            })

    # Detect repeated routing patterns
    for edge in graph.edges:
        if graph[edge[0]][edge[1]]["weight"] > 10000:  # Example threshold
            suspicious_clusters.append({
                "type": "repeated_routing",
                "accounts": edge,
                "risk_level": "MEDIUM"
            })

    return suspicious_clusters

# Example usage
if __name__ == "__main__":
    transactions = [
        ("A", "B", 5000),
        ("B", "C", 7000),
        ("C", "A", 10000),
        ("D", "E", 20000),
        ("E", "F", 15000),
        ("F", "D", 25000),
        ("G", "H", 3000),
        ("H", "I", 4000),
        ("I", "G", 5000)
    ]

    graph = build_transaction_graph(transactions)
    clusters = detect_suspicious_clusters(graph)
    for cluster in clusters:
        print(cluster)