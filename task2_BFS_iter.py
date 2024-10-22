from collections import deque

# Імпорт графа з task1
from task1 import graph_no_weights

# Створимо новий словник без ваг для BFS
# graph_no_weights = {node: [neighbor for neighbor, weight in neighbors] for node, neighbors in graph.items()}

# Перевіримо, що всі вузли мають записи у словнику
for node in graph_no_weights:
    print(f"{node}: {graph_no_weights[node]}")


# Алгоритм BFS
def bfs_iterative(graph, start):
    visited = set()  # Ініціалізація порожньої множини для зберігання відвіданих вершин
    queue = deque([start])  # Ініціалізація черги з початковою вершиною

    while queue:  # Поки черга не порожня, продовжуємо обхід
        vertex = queue.popleft()  # Вилучаємо першу вершину з черги
        if vertex not in visited:  # Перевіряємо, чи була вершина відвідана раніше
            # print(vertex, end=" ")  # Якщо не була відвідана, друкуємо її
            visited.add(vertex)  # Додаємо вершину до множини відвіданих вершин
            queue.extend(set(graph[vertex]) - visited)  # Додаємо всіх невідвіданих сусідів вершини до кінця черги

    return visited  # Повертаємо множину відвіданих вершин після завершення обходу


# Запуск алгоритму BFS
result = bfs_iterative(graph_no_weights, "Київ")
print(f"Порядок відвідування вузлів: {result}")
