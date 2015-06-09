__author__ = 'percentcer'
# Chapter 4
# Graphs

from collections import deque
from logic.linked_lists import Node

class NotSupportedError(Exception):
    pass

class TreeNode(object):
    def __init__(self, data):
        self._children = []
        self._data = data
        self._parent = None

    def __eq__(self, other):
        if other is None:
            return False

        return self._data == other.data and self.children == other.children

    def add_child(self, other):
        self._children.append(other)
        other._parent = self

    def is_leaf(self):
        return not any(self._children)

    @property
    def parent(self):
        return self._parent

    def is_root(self):
        return self._parent is None

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children):
        self._children = children
        for c in children:
            c._parent = self

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

    def __str__(self):
        return "{} ({}, {})".format(self.data, self.left, self.right)

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.data < other.data

    def __iter__(self):
        if self.left:
            for node in self.left:
                yield node

        yield self

        if self.right:
            for node in self.right:
                yield node

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
        if node is not None:
            node._parent = self

    def has_right(self):
        return self.right is not None

    @property
    def left(self):
        return self._children[0]

    @left.setter
    def left(self, node):
        self._children[0] = node
        if node is not None:
            node._parent = self

    def has_left(self):
        return self.left is not None


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

    ret.append(root)

    if root.right:
        ret.extend(in_order(root.right))

    return ret

def pre_order(root):
    if not isinstance(root, BinaryTreeNode):
        raise ValueError("Only binary nodes are supported!")

    ret = [root]

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

    ret.append(root)

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

def has_route(start, end):
    visited = set()
    next_nodes = deque(start.children)

    # nodes are unhashable, so let's use a simplified representation to track whether we've visited it
    def rep(node):
        return node.data, tuple(n.data for n in node.children)

    while next_nodes:
        current = next_nodes.popleft()

        if rep(current) in visited:
            continue

        if current == end:
            return True

        visited.add(rep(current))
        next_nodes.extend(current.children)

    return False

def make_tree_from_sorted(sa):
    if len(sa) == 1:
        return BinaryTreeNode(sa[0])

    midpoint = len(sa)//2
    r = BinaryTreeNode(sa[midpoint])
    r.left = make_tree_from_sorted(sa[:midpoint])
    if midpoint + 1 < len(sa):
        r.right = make_tree_from_sorted(sa[midpoint+1:])

    return r

def linked_rows(bst):
    rows = {}

    def dfs(t, d):
        head = rows.get(d)
        if head:
            head.append(Node(t.data))
        else:
            rows[d] = Node(t.data)
        for c in t.children:
            dfs(c, d + 1)

    dfs(bst, 0)

    return rows

def next_value(node):
    if node.right is not None:
        return min(node.right)

    cur = node

    while cur.parent is not None:
        cur = cur.parent
        if cur.data > node.data:
            return cur

    # else, we hit root and return None

def common_ancestor(left, right):

    # discovered node IDs
    ld = set()
    rd = set()

    while True:
        if left is right:
            return left
        elif left.is_root() and right.is_root():
            # disjoint trees, weird
            return None

        lid = id(left)
        rid = id(right)

        ld.add(lid)
        rd.add(rid)

        if lid in rd:
            return left
        if rid in ld:
            return right

        if left.parent:
            left = left.parent
        if right.parent:
            right = right.parent
