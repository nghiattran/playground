class Node:
    color = 'white'
    distance = None
    adjacencies = None
    parent = None
    visit_time = None
    name = None
    finish_time = None

    def __init__(self, name):
        self.name = name
        self.adjacencies = []

    def connect(self, node):
        self.adjacencies.append(node)
        node.adjacencies.append(self)

class Graph:
    nodes = []

    def addNode(self, node):
        self.nodes.append(node)

def BFS(graph, node):
    node.color = 'gray'
    node.distance = 0
    queue = [node]

    while len(queue) > 0:
        tmp_node = queue[0]
        for node in tmp_node.adjacencies:
            if node.color == 'white':
                node.color = 'gray'
                node.parent = tmp_node
                node.distance = tmp_node.distance + 1
                queue.append(node)
        queue.pop(0)
        tmp_node.color = 'black'

nodes = []

r = Node('r')
v = Node('v')
s = Node('s')
w = Node('w')
t = Node('t')
x = Node('x')
u = Node('u')
y = Node('y')

r.connect(v)
s.connect(r)
s.connect(w)
w.connect(t)
w.connect(x)
t.connect(u)
t.connect(x)
u.connect(y)
x.connect(y)

graph = Graph()
graph.nodes = [r, v, s, w, t, x, u, y]

BFS(graph, s)

for node in graph.nodes:
    print(node.name, node.distance)