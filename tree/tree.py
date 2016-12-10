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

def add_tree(values, root = None):
    if len(values) == 0:
        return

    pivot = int(len(values) / 2)
    root = tree_insert(root, Node(values[pivot]))
    add_tree(values[: pivot], root)
    add_tree(values[pivot + 1 :], root)
    return root

root = add_tree([1,2 ,3 ,4 ,5 ,6])