import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="#aaaaaa"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap(arr):
    nodes = [Node(val) for val in arr]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None

def get_color(index, total, cmap_name='viridis'):
    cmap = plt.get_cmap(cmap_name)
    return mcolors.rgb2hex(cmap(index / total))

def dfs(node, color_idx, total_nodes):
    if node:
        node.color = get_color(color_idx[0], total_nodes)
        color_idx[0] += 1
        draw_tree(root)
        dfs(node.left, color_idx, total_nodes)
        dfs(node.right, color_idx, total_nodes)

def bfs(node):
    queue = [node]
    total_nodes = count_nodes(node)
    color_idx = 0
    while queue:
        current = queue.pop(0)
        current.color = get_color(color_idx, total_nodes)
        color_idx += 1
        draw_tree(root)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Приклад масиву для бінарної купи
heap_array = [0, 1, 4, 5, 10, 3]

# Побудова та відображення бінарної купи
root = build_heap(heap_array)

# Обхід в глибину (DFS)
print("Обхід в глибину (DFS):")
color_idx = [0]
dfs(root, color_idx, count_nodes(root))

# Відновлення дерева до початкового стану перед обходом в ширину
root = build_heap(heap_array)

# Обхід в ширину (BFS)
print("Обхід в ширину (BFS):")
bfs(root)
