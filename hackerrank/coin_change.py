dict = {}
def solve(n, c, start=0):
  state = '%d-%d' % (n, start)
  if n == 0:
    return 0
  if len(c) == 0:
    return 0

  if state in dict:
    return dict[state]

  cnt = 0
  for i in range(start, len(c)):
    coin = c[i]
    if n == coin:
      cnt += 1
    elif n > coin:
      cnt += solve(n - coin, c, i)
  dict[state] = cnt
  return cnt

def test(n, c, e):
  r = solve(n, c)
  assert r == e

def parse(f, s):
  n, m = [int(i) for i in f.split(' ')]
  c = sorted([int(i) for i in s.split(' ')])
  return n, m, c

f = '4 3'
s = '1 2 3'
e = 4
n, m, c = parse(f, s)
test(n, c, e)

dict = {}
f = '10 4'
s = '2 3 5 6'
e = 5
n, m, c = parse(f, s)
test(n, c, e)