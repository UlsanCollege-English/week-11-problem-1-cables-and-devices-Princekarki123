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
    # Pseudocode:
    # 1. Create empty dictionary: graph = {}
    # 2. Loop over each (u, v) in edges
    # 3. If u not in graph, add graph[u] = []
    # 4. Append v to graph[u]
    # 5. If undirected: also add v->u (same process)
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

        # Ensure the target node exists in the graph even for directed graphs.
        # For directed graphs this will leave an empty neighbor list for v;
        # for undirected graphs we then add the reverse edge.
        if v not in graph:
            graph[v] = []

        if not directed:
            graph[v].append(u)

    return graph


def degree_dict(graph):
    """Return a dictionary: node -> degree (number of neighbors).

    For directed graphs: out-degree.
    For undirected graphs: standard degree.
    """
    degrees = {}
    for node in graph:
        degrees[node] = len(graph[node])
    return degrees


if __name__ == "__main__":
    # Optional manual check
    sample = [('PC1', 'SW1'), ('SW1', 'PR1'), ('PR1', 'PC2')]
    print("Sample edges:", sample)

    g = build_graph(sample, directed=False)
    print("Graph:", g)

    d = degree_dict(g)
    print("Degrees:", d)
