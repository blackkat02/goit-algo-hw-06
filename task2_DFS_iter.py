from task1 import graph_no_weights

# Перевіримо, що всі вузли мають записи у словнику
for node in graph_no_weights:
    print(f"{node}: {graph_no_weights[node]}")


def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            # print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))

    return visited


# Виклик функції DFS
result = dfs_iterative(graph_no_weights, "Київ")
print(f"Порядок відвідування вузлів: {result}")
