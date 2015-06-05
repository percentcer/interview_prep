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
        return self._data == other.data and self.children == other.children

    def add_child(self, other):
        self._children.append(other)

    def is_leaf(self):
        return not any(self._children)

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

    def __eq__(self, other):
        if not isinstance(other, BinaryTreeNode):
            return super().__eq__(other)
        else:
            return self._children == other._children

    def add_child(self, other):
        raise NotSupportedError("Please use left or right for BinaryTreeNode")

    @property
    def children(self):
        return [c for c in self._children if c is not None]

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
    if rep is None or rep is ():
        return None

    data, left, right = rep

    ret = BinaryTreeNode(data)
    ret.left = binary_tree_constructor(left)
    ret.right = binary_tree_constructor(right)

    return ret

def tree_constructor(rep):
    if rep is None or rep is ():
        return None

    data, children = rep
    ret = TreeNode(data)
    for c in children:
        ret.add_child(tree_constructor(c))
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

def depth_of_leaves(root, n=0):
    if root is None:
        return []
    elif root.is_leaf():
        return [n]

    ret = []
    for c in root.children:
        ret.extend(depth_of_leaves(c, n+1))
    return ret

def is_balanced(root):
    if root is None:
        return True
    dleaves = depth_of_leaves(root)
    return max(dleaves) - min(dleaves) <= 1
