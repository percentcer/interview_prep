__author__ = 'percentcer'
# Chapter 4
# Graphs

class NotSupportedError(Exception):
    pass

class TreeNode(object):
    def __init__(self, data):
        self._children = []
        self._data = data

    def __eq__(self, other):
        return self._data == other.data and self._children == other.children

    def add_child(self, other):
        self._children.append(other)

    def is_leaf(self):
        return not len(self._children)

    @property
    def children(self):
        return self._children

    @property
    def data(self):
        return self._data


class BinaryTreeNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)
        self._children = [None, None]

    def add_child(self, other):
        raise NotSupportedError("Please use add_left or add_right for BinaryTreeNode")

    @property
    def right(self):
        return self._children[1]

    @right.setter
    def right(self, node):
        self._children[1] = node

    @property
    def left(self):
        return self._children[0]

    @left.setter
    def left(self, node):
        self._children[0] = node


def node_cons(obj):
    data, left, right = obj
    ret = BinaryTreeNode(data)
    ret.left = left
    ret.right = right
    return ret

def binary_tree_constructor(rep):
    if rep is None:
        return None

    data, left, right = rep

    ret = BinaryTreeNode(data)
    ret.left = binary_tree_constructor(left)
    ret.right = binary_tree_constructor(right)

    return ret

def in_order(root):
    if not isinstance(root, BinaryTreeNode):
        raise ValueError("Only binary nodes are supported!")

    ret = []

    if root.left:
        ret.extend(in_order(root.left))

    ret.append(root.data)

    if root.right:
        ret.extend(in_order(root.right))

    return ret

def pre_order(root):
    if not isinstance(root, BinaryTreeNode):
        raise ValueError("Only binary nodes are supported!")

    ret = [root.data]

    if root.left:
        ret.extend(pre_order(root.left))

    if root.right:
        ret.extend(pre_order(root.right))

    return ret

def post_order(root):
    if not isinstance(root, BinaryTreeNode):
        raise ValueError("Only binary nodes are supported!")

    ret = []

    if root.left:
        ret.extend(pre_order(root.left))

    if root.right:
        ret.extend(pre_order(root.right))

    ret.append(root.data)

    return ret