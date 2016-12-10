class Node:
    _left_child = None
    _right_child = None
    _parent = None

    def __init__(self, key):
        self._key = key

    def get_key(self):
        return self._key

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def set_right_child(self, child):
        self._right_child = child

    def set_left_child(self, child):
        self._left_child = child

    def get_left_child(self):
        return self._left_child

    def get_right_child(self):
        return self._right_child


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def tree_search(node, value):
    if node is None or value == node.get_key():
        return node

    if value < node.get_key():
        return tree_search(node.get_left_child(), value)
    else:
        return tree_search(node.get_right_child(), value)


def tree_insert(root, new_node):
    y = None
    x = root

    while x is not None:
        y = x
        if new_node.get_key() < x.get_key():
            x = x.get_left_child()
        else:
            x = x.get_right_child()

    new_node.set_parent(y)

    if y is None:
        root = new_node
    elif new_node.get_key() < y.get_key():
        y.set_left_child(new_node)
    else:
        y.set_right_child(new_node)

    return root


def tree_maximum(node):
    y = node
    while y.get_right_child() is not None:
        y = y.get_right_child()
    return y


def tree_minimum(node):
    y = node
    while y.get_left_child() is not None:
        y = y.get_left_child()
    return y


def tree_successor(node):
    if node.get_right_child() is not None:
        return tree_minimum(node.get_right_child())
    else:
        y = node.get_parent()
        while y is not None and node == y.get_right_child():
            node = y
            y = y.get_parent()
        return y


def tree_predecessor(node):
    pass


# tree_search([5, 3, 13, 10, 14, 11, 12], 0, 14)

arr = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
nodes = []
root = None
for e in arr:
    nodes.append(Node(e))
    root = tree_insert(root, nodes[len(nodes) - 1])

print(nodes[10].get_key(), tree_successor(nodes[10]).get_key())

print(tree_search(nodes[0], 2).get_parent().get_key())