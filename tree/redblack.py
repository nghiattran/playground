# 1. every node is either red or black
# 2. root is black
# 3. every leaf is black
# 4. if a node is red, both its children are black
# 5. every path from node to a descendant leaf contains same number of black nodes

class NILL:
    pass


class Tree:
    root = None
    nill = NILL()


class Node:
    left = None
    right = None
    parent = None


def left_rotate(tree, node):
    y = node.right
    node.right = y.left
    y.left.parent = node
    y.parent = node.parent

    if node.parent is None:
        tree.root = y
    elif node == node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y

    y.left = node
    node.parent = y


def right_rotate(tree, node):
    y = node.right
    node.left = y.right
    y.right.parent = node
    y.parent = node.parent

    if node.parent is None:
        tree.root = y
    elif node == node.parent.right:
        node.parent.right = y
    else:
        node.parent.left = y

    y.right = node
    node.parent = y