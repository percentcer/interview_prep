import unittest

from logic.graphs import *

class TestGraphs(unittest.TestCase):
    def setUp(self):
        self.unordered_binary_tree = binary_tree_constructor((42, (0, None, None), (1, None, None)))
        self.unbalanced_binary_tree = binary_tree_constructor((0, (1, (2, (3, (), ()), ()), ()), (11, (), ())))
        self.unbalanced_tree = tree_constructor(
            (0, (
                (1, ((2, ((3, ()),)),)),
                (11, ()),
                (111, ((222, ((333, ()),)),))
            ))
        )
        self.empty_tree = tree_constructor(())

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

    def test_depth_of_leaves(self):
        self.assertEqual(depth_of_leaves(self.unordered_binary_tree), [1, 1])
        self.assertEqual(depth_of_leaves(self.unbalanced_binary_tree), [3, 1])
        self.assertEqual(depth_of_leaves(self.unbalanced_tree), [3, 1, 3])
        self.assertEqual(depth_of_leaves(self.empty_tree), [])

    def test_is_balanced(self):
        self.assertFalse(is_balanced(self.unbalanced_binary_tree))
        self.assertFalse(is_balanced(self.unbalanced_tree))
        self.assertTrue(is_balanced(self.unordered_binary_tree))
        self.assertTrue(is_balanced(self.empty_tree))

    def test_binary_add_failure(self):
        b = BinaryTreeNode(0)
        self.assertRaises(NotSupportedError, b.add_child, 1)
