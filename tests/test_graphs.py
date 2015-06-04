import unittest

from logic.graphs import *

class TestGraphs(unittest.TestCase):
    def setUp(self):
        self.unordered_binary_tree = binary_tree_constructor((42, (0, None, None), (1, None, None)))

    def tearDown(self):
        pass

    def test_node_construction(self):
        t = (42, None, None)

        self.assertEqual(node_cons(t), BinaryTreeNode(42))

    def test_hierarchical_node_equality(self):
        btn = BinaryTreeNode(42)
        btn.left = BinaryTreeNode(0)
        btn.right = BinaryTreeNode(1)

        self.assertEqual(self.unordered_binary_tree, btn)

    def test_in_order(self):
        desired = [0, 42, 1]
        self.assertEqual(in_order(self.unordered_binary_tree), desired)

    def test_pre_order(self):
        desired = [42, 0, 1]
        self.assertEqual(pre_order(self.unordered_binary_tree), desired)

    def test_post_order(self):
        desired = [0, 1, 42]
        self.assertEqual(post_order(self.unordered_binary_tree), desired)