class Node:
    name = None
    adjacencies = None
    adjacent_list = None
    distance = None
    parent = None
    
    def __init__(self, name):
        self.name = name
        self.adjacencies = []
        self.adjacent_list = {}
        self.distance = 999999

    def connect(self, node, distance):
        self.adjacencies.append(node)
        self.adjacent_list[node] = distance

    def distance_to(self, node):
        return self.adjacent_list.get(node)

def extract_min(Q):
    min = None
    for index, node in enumerate(Q):
        if min == None or node.distance < Q[min].distance:
            min = index
    return Q.pop(min)

def relax(node1, node2):
    if node2.distance > node1.distance + node1.distance_to(node2):
        node2.distance = node1.distance + node1.distance_to(node2)
        node2.parent = node1

def dijkstra(Q):
    S = []
    while len(Q) > 0:
        node = extract_min(Q)
        S.append(node)
        for subnode in node.adjacencies:
            relax(node, subnode)

    return S

s = Node('s')
t = Node('t')
y = Node('y')
x = Node('x')
z = Node('z')

s.connect(t, 10)
s.connect(y, 5)

t.connect(y, 2)
t.connect(x, 1)

y.connect(z, 2)
y.connect(t, 3)
y.connect(x, 9)

x.connect(z, 4)

z.connect(x, 6)
z.connect(s, 7)

Q = [s, t, y, x, z]

s.distance = 0
for node in dijkstra(Q):
    print(node.name, node.distance)