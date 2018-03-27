class GraphNode:
    def __init__(self, data):
        self.data = data  # contains the data
        self.children = list()  # contains the reference to the left child

    def __repr__(self):
        return f"treeval = {self.data}"

def dfs_path(root):
    path = list()
    node_list = list()
    node_list.append(root)
    visited = set()
    while len(node_list) > 0:
        node = node_list.pop()
        path.append(node.data)
        visited.add(node)
        for child in node.children:
            if child in visited:
                continue
            node_list.append(child)
    return path


import queue


def bfs_path(root):
    path = list()
    node_queue = queue.Queue()
    node_queue.put(root)
    visited = set()
    while not node_queue.empty():
        node = node_queue.get()
        visited.add(node)
        path.append(node.data)
        for child in node.children:
            if child in visited:
                continue
            node_queue.put(child)
    return path


root = GraphNode(0)
child1 = GraphNode(1)
child2 = GraphNode(2)
root.children = [child1]
child1.children = [child2, GraphNode(3), GraphNode(4)]
child2.children = [root, GraphNode(5), GraphNode(6)]

print(bfs_path(root))
print(dfs_path(root))