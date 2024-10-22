from collections import deque
from task1 import graph_no_weights


# Перевіримо, що всі вузли мають записи у словнику
for node in graph_no_weights:
    print(f"{node}: {graph_no_weights[node]}")


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        # print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

    return visited

# Запуск рекурсивного алгоритму BFS
result = bfs_recursive(graph_no_weights, deque(["Київ"]))
print(f"Порядок відвідування вузлів: {result}")