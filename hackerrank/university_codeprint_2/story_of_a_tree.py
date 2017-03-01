import time

def printTree(tree):
  nodeNames = tree.dict.keys()
  for nn in nodeNames:
    parent = tree.dict[nn].parent
    if parent is None:
      val = 0
    else:
      val = parent.val
    print(nn, val)
  print()

# n^2 implementation
class NodePool:
  def __init__(self):
    self.dict = {}

  def create(self, val):
    if val in self.dict: return self.dict[val]

    self.dict[val] = Node(val)
    return self.dict[val]

  def createTree(self, links):
    self.dict = {}
    for l in links:
      p, c = l
      self.createPair(p, c)

  def createPair(self, parent, child):
    parent = self.create(parent)
    child = self.create(child)
    child.link(parent, True)
    parent.link(child)

  def pickRoot(self, val):
    for node in self.dict.values():
      node.inOrder = False
    self.dict[val].pickRoot()

  def check(self, relations):
    count = 0
    for r in relations:
      p, c = r
      if self.dict[c].isParent(p):
        count += 1
    return count


class Node:
  def __init__(self, val):
    self.inOrder = False
    self.val = val
    self.level = -1
    self.conn = {}
    self.parent = None

  def isParent(self, parentVal):
    return self.parent is not None and self.parent.val == parentVal

  def link(self, node, isParent=False):
    self.conn[node.val] = node

    if isParent:
      self.parent = node

  def pickRoot(self):
    if self.parent is None:
      return
    self.parent.reRoute(self)
    self.parent = None

  def reRoute(self, parent):
    if self.inOrder:
      return

    self.inOrder = True
    if self.parent is not None:
      self.parent.reRoute(self)
    self.parent = parent

# http://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

pool = NodePool()

threshold = 2
#
links = [[1, 2], [1, 3], [3, 4], [4, 5], [4, 6],[6, 7], [6, 8], [3, 9]]
guesses = [[1, 2], [3, 4]]

# links = [[1, 2], [1, 3]]
# guesses = [[1, 2], [1, 3]]

# start = time.time()
#
# pool.createTree(links)
# nodeNames = list(pool.dict.keys())
#
# rightCnt = 0
# for name in nodeNames:
#   pool.pickRoot(name)
#   count = pool.check(guesses)
#   rightCnt += 1 if count >= threshold else 0
#
#   print(name, 'tree')
#   printTree(pool)
#
# divisor = gcd(rightCnt, len(nodeNames))
#
# print("%d/%d" % (int(rightCnt / divisor), int(len(nodeNames) / divisor)))
#
# print(time.time() - start)

n,k,q = 3,1,3
a = [1, 2, 3]
ms = [0, 1, 2]

indexes = []
for i in range(n):
  indexes.append((i - k) % n)
print(indexes)
for a0 in range(q):
    # m = int(input().strip())
    m =ms[a0]
    print(a[indexes[m]])