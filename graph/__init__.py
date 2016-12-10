class Node:
    color = 'white'
    distance = None
    adjacencies = []
    parent = None
    visit_time = None
    name = None

    def __init__(self, name):
        self.name = name

    def connect(self, node):
        self.adjacencies.append(node)
        node.adjacencies.append(self)

class Graph:
    nodes = []

    def addNode(self, node):
        self.nodes.append(node)