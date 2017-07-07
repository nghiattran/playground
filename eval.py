class Node(object):
    """
    Node in binary tree
    """
    def __init__(self, val):
        self.value = val
        self._l = None
        self._r = None
        self.parent = None

    @property
    def left(self):
        return self._l

    @left.setter
    def left(self, value):
        value.parent = self
        self._l = value

    @property
    def right(self):
        return self._r

    @right.setter
    def right(self, value):
        value.parent = self
        self._r = value


class ValueNode(Node):
    """
    Datatype for Value (in this case, integers) nodes
    """
    pass


class OpNode(Node):
    """
    Datatype for Operation nodes
    """
    pass


class AddNode(OpNode):
    """
    Datatype for Addition (+) operation nodes
    """
    def add_children(self, left, right):
        self._l = left
        self._r = right
        return self


class MulNode(OpNode):
    """
    Datatype for Multiplycation (*) operation nodes
    """
    def add_children(self, root, right):
        if isinstance(root, ValueNode):
            self._l = root
            self._r = right
            return self

        self._l = root.right
        self._r = right
        root.right = self
        return self.parent


def next_node(s, start):
    """
    Parse next node in expression

    :param s:           given expression..
    :param start:       index of current parsing location.
    :return:            a Node and current parsing location.
    """
    if s[start] == '+':
        return AddNode(s[start]), start + 1
    elif s[start] == '*':
        return MulNode(s[start]), start + 1

    val = s[start]
    i = start + 1
    while i < len(s):
        if s[i] == '+' or s[i] == '*':
            break
        else:
            val += s[i]
        i+=1

    try:
        value = int(val)
    except Exception as e:
        raise ValueError('%s is not a valid integer.' % str(val))

    return ValueNode(value), i

def evaluate(s):
    """
    Encode infix arithmetic expressions on integers using binary tree.

    :param s:   an expression as string.
    :return:    root node of the binary tree
    """
    # Remove all white spaces
    s = "".join(s.split())

    root = None
    i = 0
    while i < len(s):
        # Get next node in given string
        node, i = next_node(s, i)
        if not root:
            # If the first node is not a ValueNode, the given string is not a valid expression
            if not isinstance(node, ValueNode):
                raise ValueError('%s is not a valid expression.' % str(s))
            else:
                root = node
        elif isinstance(node, OpNode):
            # print(s[i], i, s)
            node1, i = next_node(s, i)
            root = node.add_children(root, node1)
        else:
            raise ValueError('%s is not a valid expression.' % str(s))

    return root

s = '1 + 4 * 6 + 9 + 2'
root = evaluate(s)
assert root.right.value == 2
assert root.left.left.right.left.value == 4


s = '1 *2 *3'
root = evaluate(s)
assert root.right.right.value == 3

s = '1 + 4 * 6 + 9 + 2 + 10 + 56 * 9 * 5'
root = evaluate(s)
assert root.right.left.left.value == 56
assert root.left.left.left.right.value == 9
assert root.left.left.left.left.right.left.value == 4
