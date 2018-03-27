from binary_tree import BinaryTreeNode


def get_values_by_level(root: BinaryTreeNode):
    import queue
    values = []
    if root is None:
        return values
    node_queue = queue.Queue()
    node_queue.put(root)
    while not node_queue.empty():
        node = node_queue.get()
        values.append(node.data)
        if node.left is not None:
            node_queue.put(node.left)
        if node.right is not None:
            node_queue.put(node.right)
    return values
