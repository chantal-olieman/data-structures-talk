class TreeNode:
    def __init__(self, data):
        self.data = data  # contains the data
        self.children = list()  # contains the reference to the left child

    def __repr__(self):
        return f"treeval = {self.data}"


def dfs_path(root):
    path = list()
    node_list = list()
    node_list.append(root)
    while len(node_list) > 0:
        node = node_list.pop()
        path.append(node.data)
        for child in node.children:
            node_list.append(child)
    return path


import queue


def bfs_path(root):
    path = list()
    node_queue = queue.Queue()
    node_queue.put(root)
    while not node_queue.empty():
        node = node_queue.get()
        path.append(node.data)
        for child in node.children:
            node_queue.put(child)
    return path


root = TreeNode(0)
child1 = TreeNode(1)
child2 = TreeNode(2)
root.children = [child1]
child1.children = [child2, TreeNode(3), TreeNode(4)]
child2.children = [TreeNode(5), TreeNode(6)]

print(bfs_path(root))
print(dfs_path(root))