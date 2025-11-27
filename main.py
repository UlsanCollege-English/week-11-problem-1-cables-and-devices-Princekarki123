"""
HW01 — Cables and Devices

Implement:
- build_graph(edges, directed=False)
- degree_dict(graph)

Do NOT add type hints. Use only the standard library.
"""

def build_graph(edges, directed=False):
    """Return a dictionary: node -> list of neighbors.

    edges: list of (u, v) pairs.
    directed: if True, add only u->v; if False, add both u->v and v->u.
    """
    graph = {}

    for u, v in edges:
        # Ensure key exists
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Add u -> v
        graph[u].append(v)

        # If undirected, also add v -> u
        if not directed:
            graph[v].append(u)

    return graph


def degree_dict(graph):
    """Return a dictionary: node -> degree (number of neighbors).

    For directed graphs, this is out-degree.
    For undirected graphs, this is the usual degree.
    """
    degrees = {}

    for node in graph:
        degrees[node] = len(graph[node])

    return degrees


if __name__ == "__main__":
    # Optional manual check
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    print("Sample edges:", sample)
    # Uncomment to test manually:
    # g = build_graph(sample, directed=False)
    # print("Graph:", g)
    # print("Degrees:", degree_dict(g))
    pass
