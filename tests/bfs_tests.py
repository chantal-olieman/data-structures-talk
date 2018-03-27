import unittest
from src.bfs import get_values_by_level, BinaryTreeNode


class TestBFS(unittest.TestCase):

    def test_empty_input(self):
        root = None
        result = get_values_by_level(root)
        self.assertEqual([], result)

    def test_simple_tree(self):
        root = BinaryTreeNode(3)
        root.left = BinaryTreeNode(5)
        root.left.left = BinaryTreeNode(6)
        root.right = BinaryTreeNode(4)
        self.assertEqual([3, 5, 4, 6], get_values_by_level(root))

    def test_example_tree(self):
        root = BinaryTreeNode(2)
        root.left = BinaryTreeNode(7)
        root.left.left = BinaryTreeNode(2)
        root.left.right = BinaryTreeNode(6)
        root.left.right.left = BinaryTreeNode(5)
        root.left.right.right = BinaryTreeNode(11)
        root.right = BinaryTreeNode(5)
        root.right.right = BinaryTreeNode(9)
        root.right.right.left = BinaryTreeNode(4)
        self.assertEqual([2, 7, 5, 2, 6, 9, 5, 11, 4], get_values_by_level(root))

    def left_tree(self):
        root = BinaryTreeNode(2)
        root.left = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        root.left.left.left = BinaryTreeNode(5)
        root.left.left.left.left = BinaryTreeNode(6)
        root.left.left.left.left.left = BinaryTreeNode(7)
        root.left.left.left.left.left.left = BinaryTreeNode(8)
        root.left.left.left.left.left.left.left = BinaryTreeNode(9)
        root.left.left.left.left.left.left.left.left = BinaryTreeNode(10)
        root.left.left.left.left.left.left.left.left.left = BinaryTreeNode(11)
        root.left.left.left.left.left.left.left.left.left.left = BinaryTreeNode(12)
        root.left.left.left.left.left.left.left.left.left.left.left = BinaryTreeNode(13)
        self.asserEqual([2, 7, 5], get_values_by_level(root))
