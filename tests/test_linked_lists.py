import unittest

from logic.linked_lists import *

class TestListProblems(unittest.TestCase):
    def setUp(self):
        self.nodes = Node.gen_nodes(n=10)
        self.duped = Node.gen_nodes(n=10)
        self.duped.append(Node.gen_nodes(n=10))

    def test_remove_duplicates(self):
        remove_duplicates(self.duped)
        self.assertEqual(self.duped, self.nodes)

    def test_remove_duplicates_ip(self):
        remove_duplicates_ip(self.duped)
        self.assertEqual(self.duped, self.nodes)

    def test_n_to_last(self):
        target = Node.gen_nodes(n=3)
        self.assertEqual(target, n_to_last(self.nodes, 3))

    def test_delete_node(self):
        delete_node(self.nodes.next)
        self.assertEqual(self.nodes, Node.from_list([10,8,7,6,5,4,3,2,1]))

    def test_add_lists(self):
        left = Node.gen_nodes(n=5).reversed()
        right = Node.gen_nodes(n=5).reversed()
        self.assertEqual(add_lists(left, right), Node.from_list([2,4,6,8,0,1]))

        left = Node.gen_nodes(n=5).reversed()
        right = Node.gen_nodes(n=8).reversed()
        self.assertEqual(add_lists(left, right), Node.from_list([2,4,6,8,0,7,7,8]))
