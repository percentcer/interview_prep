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
        self.binary_search_tree = binary_tree_constructor(
            (42, (40, (37, (16, (), ()), ()), (41, (), ())), (58, (50, (49, (), ()), ()), (67, (), ())))
        )
        self.empty_tree = tree_constructor(())
        # 0_
        # |  \
        # 1   2 _
        # | / | \|
        # 3   4  5
        nodes = [TreeNode(i) for i in range(6)]
        nodes[0].children = [nodes[1], nodes[2]]
        nodes[1].children = [nodes[3]]
        nodes[2].children = [nodes[3], nodes[4], nodes[5]]
        nodes[5].children = [nodes[2]]
        self.looped_dag = nodes[0]
        self.dag_nodes = nodes

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
        self.assertEqual([d.data for d in in_order(self.unordered_binary_tree)], desired)

    def test_pre_order(self):
        desired = [42, 0, 1]
        self.assertEqual([d.data for d in pre_order(self.unordered_binary_tree)], desired)

    def test_post_order(self):
        desired = [0, 1, 42]
        self.assertEqual([d.data for d in post_order(self.unordered_binary_tree)], desired)

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

    def test_has_route(self):
        self.assertTrue(has_route(self.dag_nodes[0], self.dag_nodes[3]))
        self.assertTrue(has_route(self.dag_nodes[0], self.dag_nodes[5]))
        self.assertTrue(has_route(self.dag_nodes[5], self.dag_nodes[2]))
        self.assertTrue(has_route(self.dag_nodes[5], self.dag_nodes[3]))
        self.assertTrue(has_route(self.dag_nodes[5], self.dag_nodes[5]))
        self.assertFalse(has_route(self.dag_nodes[5], self.dag_nodes[0]))
        self.assertFalse(has_route(self.dag_nodes[2], self.dag_nodes[1]))

    def test_make_tree(self):
        self.assertEqual(self.binary_search_tree, make_tree_from_sorted([16, 37, 40, 41, 42, 49, 50, 58, 67]))

    def test_linked_rows(self):
        actual = linked_rows(self.binary_search_tree)
        desired = {
            0: Node(42),
            1: Node.from_list([40, 58]),
            2: Node.from_list([37, 41, 50, 67]),
            3: Node.from_list([16, 49])
        }
        self.assertEqual(actual, desired)

    def test_next_value(self):
        nodes = in_order(self.binary_search_tree)
        _40 = nodes[2]
        _41 = nodes[3]
        _42 = nodes[4]
        _49 = nodes[5]
        _67 = nodes[8]
        self.assertEqual(42, next_value(_41).data)
        self.assertEqual(50, next_value(_49).data)
        self.assertEqual(49, next_value(_42).data)
        self.assertEqual(41, next_value(_40).data)
        self.assertEqual(None, next_value(_67))

    def test_common_ancestor(self):
        nodes = in_order(self.binary_search_tree)
        _16 = nodes[0]
        _37 = nodes[1]
        _40 = nodes[2]
        _41 = nodes[3]
        _42 = nodes[4]
        _49 = nodes[5]
        _50 = nodes[6]
        _58 = nodes[7]
        _67 = nodes[8]
        self.assertEqual(common_ancestor(_16, _41), _40)
        self.assertEqual(common_ancestor(_16, _49), _42)
        self.assertEqual(common_ancestor(_16, _42), _42)
        self.assertEqual(common_ancestor(_16, _37), _37)
        self.assertEqual(common_ancestor(_37, _37), _37)
        self.assertEqual(common_ancestor(_50, _67), _58)
