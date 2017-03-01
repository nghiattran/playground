class Node:
  def __init__(self, val):
    self.val = val
    self.conn = []
    self.dist = -1
    self.visited = False

  def link(self, node):
    self.conn.append(node)

def solve(m, n, e, s):
  nodes = {}
  for i in range(n):
    nodes[i + 1] = Node(i + 1)

  for edge in e:
    fi, se = edge
    nodes[fi].link(nodes[se])
    nodes[se].link(nodes[fi])

  nodes[s].dist = 0
  stack = [nodes[s]]
  while len(stack) != 0:
    cur = stack[0]
    cur.visited = True

    for n in cur.conn:
      if n.visited == False:
        n.visited = True
        stack.append(n)
        n.dist = cur.dist + 6
    stack = stack[1:]

  del nodes[s]
  return ' '.join([str(nodes[n].dist) for n in nodes])


def test(m, n, e, s, exp):
  res = solve(m, n, e, s)
  assert len(res) == exp
  for i in range(len(exp)):
    assert res[i] == exp[i]


n, m = 4, 2
e = [[1, 2], [1, 3], [2, 3]]
s = 1

print(solve(m, n, e, s))