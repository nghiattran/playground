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
time = 0
def dfs(graph):
    for node in graph.nodes:
        if node.color == 'white':
            dfs_visit(node, time)

def dfs_visit(node, time):
    time += 1
    node.color = 'gray'
    node.visit_time = time

    for subnode in node.adjacencies:
        if subnode.color == 'white':
            subnode.parent = node
            time = dfs_visit(subnode, node.visit_time)

    node.color = 'black'
    node.finish_time = time + 1
    return time

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

dfs(graph)

for node in graph.nodes:
    print(node.name, node.distance, node.visit_time, node.finish_time)