from task1 import graph_no_weights


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    # print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


# Виклик функції DFS
result = dfs_recursive(graph_no_weights, "Київ")
print(f"Порядок відвідування вузлів: {result}")
