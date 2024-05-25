import heapq

class Graph:
    '''Створення класу для представлення графа'''
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))  # для неорієнтованого графа
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # для неорієнтованого графа

def dijkstra(graph, initial):
    '''Реалізація алгоритму Дейкстри з використанням бінарної купи'''
    # Ініціалізація всіх відстаней як нескінченні
    visited = {node: float('infinity') for node in graph.nodes}
    visited[initial] = 0

    path = {}

    # Використання пріоритетної черги для вибору вершини з мінімальною відстанню
    priority_queue = [(0, initial)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > visited[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            # Якщо знайдена нова коротша відстань
            if distance < visited[neighbor]:
                visited[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                path[neighbor] = current_node

    return visited, path

def print_shortest_path(graph, initial):
    '''Функція для відображення результатів'''
    distances, paths = dijkstra(graph, initial)
    for node in distances:
        print(f"Відстань від {initial} до {node}: {distances[node]}")

#Приклад використання
# Створення графа
graph = Graph()
nodes = ['A', 'B', 'C', 'D', 'E']
for node in nodes:
    graph.add_node(node)

edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1),
    ('D', 'E', 3)
]

for edge in edges:
    graph.add_edge(*edge)

# Обчислення найкоротших шляхів від початкової вершини 'A'
print_shortest_path(graph, 'A')
