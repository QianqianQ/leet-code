
# Pseudocode
# DFS(G, u):
#     u.visited = true
#     for each v ∈ G.Adj[u]:
#         if v.visited == false:
#             DFS(G, v)

# init():
#     For each u ∈ G:
#         u.visited = false
#     For each u ∈ G:
#         if u.visited == false:
#             DFS(G, u)

def dfs_recursive(graph, node, visited=None) -> None:
    if not visited:
        visited = set()

    visited.add(node)
    print(node)

    for n in graph[node]:
        if n not in visited:
            dfs_recursive(graph, n, visited)


def dfs_iterative(graph, start) -> None:
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)

        # Reverse neighbors to match recursive DFS traversal order
        for neighbor in graph[node][::-1]:
            if neighbor not in visited:
                stack.append(neighbor)


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'D': ['H', 'I'],
        'E': ['J', 'K'],
        'F': ['L', 'M'],
        'G': ['N', 'O'],
        'H': [], 'I': [], 'J': [], 'K': [],
        'L': [], 'M': [], 'N': [], 'O': []
    }

    print("DFS Recursive:")
    dfs_recursive(graph, "A")

    print("\nDFS Iterative:")
    dfs_iterative(graph, "A")
