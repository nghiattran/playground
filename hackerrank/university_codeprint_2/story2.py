MAXN = 20
COUNT = 0


class Conn:
  def __init__(self, val, next):
    self.val = val
    self.next = next

  def print(self):
    print(self.val, self.next)

class Pool:
  def __init__(self):
    self.conns = [-1] * (2 * MAXN + 10);
    self.nodes = [-1] * (MAXN + 1)
    self.count = 0

  def connect(self, x, y):
    tmp = self.count
    self.count += 1
    self.conns[tmp] = Conn(y, self.nodes[x])
    self.nodes[x] = tmp


def traversal(cur, stop, guesses, pool):
  count = 0
  i = pool.nodes[cur]
  while i != -1:
    if pool.conns[i].val == stop:
      i = pool.conns[i].next
      continue
    if '%d-%d' % (cur, pool.conns[i].val) in guesses:
      count += 1

    count += traversal(pool.conns[i].val, cur, guesses, pool)
    i = pool.conns[i].next
  return count


def traversal1(cur, stop, guesses, hit, threshold, pool):
  if stop != -1 and '%d-%d' % (cur, stop) in guesses:
    hit += 1

  count = 1 if hit >= threshold else 0
  i = pool.nodes[cur]
  while i != -1:
    if pool.conns[i].val == stop:
      i = pool.conns[i].next
      continue
    found = 1 if '%d-%d' % (cur, pool.conns[i].val) in guesses else 0
    count += traversal1(pool.conns[i].val, cur, guesses, hit - found,
                        threshold, pool)
    i = pool.conns[i].next
  return count


def solve(links, guesses, threshold, numNodes):
  guessDict = {}
  for g in guesses:
    a, b = g
    guessDict['%d-%d' % (a, b)] = g

  pool = Pool()
  for l in links:
    x, y = l
    pool.connect(x, y)
    pool.connect(y, x)

  hit = traversal(1, -1, guessDict, pool)
  count = traversal1(1, -1, guessDict, hit, threshold, pool)
  div = gcd(numNodes, count)
  return "%d/%d" % ((count / div), (numNodes / div))



# http://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
def gcd(a, b):
  """Calculate the Greatest Common Divisor of a and b.

  Unless b==0, the result will have the same sign as b (so that when
  b is divided by it, the result comes out positive).
  """
  while b:
      a, b = b, a%b
  return a

threshold = 2
links = [[1, 2], [1, 3], [3, 4]]
guesses = [[1, 2], [3, 4]]
numNodes = 4

links = [[1, 2], [1, 3]]
guesses = [[1, 2], [1, 3]]
numNodes = 3

print(solve(links, guesses, threshold, numNodes))

