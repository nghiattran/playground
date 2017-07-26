import queue
from collections import defaultdict
data = """4 6
1 2 1
1 3 3
1 4 7
2 3 2
2 4 3
3 4 3"""

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

data = data.split('\n')

n, m = [int(num) for num in data[0].split(' ')]
data = data[1:]

graph = Graph()
for i in range(m):
    start_n, end_n, w = [int(num) for num in data[i].split(' ')]
    graph.add_node(start_n)
    graph.add_node(end_n)
    graph.add_edge(start_n, end_n, w)

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path

_, path = dijsktra(graph, 1)