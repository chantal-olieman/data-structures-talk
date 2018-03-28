import unittest
from src.bfs import get_values_by_level
from src.binary_tree import BinaryTreeNode


class TestBFS(unittest.TestCase):

    def test_empty_input(self):
        root = None
        result = get_values_by_level(root)
        self.assertEqual([], result)

    def test_big_tree(self):
        root = BinaryTreeNode(0)
        root.left = BinaryTreeNode(1)
        root.right = BinaryTreeNode(2)
        root.right.left = BinaryTreeNode(5)
        root.right.right = BinaryTreeNode(6)
        root.left.right = BinaryTreeNode(4)
        root.left.left = BinaryTreeNode(3)
        root.left.left.left = BinaryTreeNode(7)
        root.left.left.right = BinaryTreeNode(8)
        root.left.right.left = BinaryTreeNode(9)
        root.left.right.right = BinaryTreeNode(10)
        root.right.left.left = BinaryTreeNode(11)
        root.right.left.right = BinaryTreeNode(12)
        root.right.right.left = BinaryTreeNode(13)
        root.right.right.right = BinaryTreeNode(14)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], get_values_by_level(root))

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

    def test_left_tree(self):
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
        self.assertEqual([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], get_values_by_level(root))



