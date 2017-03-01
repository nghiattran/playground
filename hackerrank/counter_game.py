def solve(n):
  turn = 0
  while n != 1:
    if n & (n - 1) == 0:
      n >>= 1
    else:
      hi = len(bin(n)) - 3
      n -= 1 << hi
    turn = (turn + 1) % 2

  return 'Louise' if turn == 1 else 'Richard'

def test(n, expected):
  res = solve(n)
  assert res == expected

# n = 1
# expected = 'Richard'
# test(n, expected)
#
# n = 6
# expected = 'Richard'
# test(n, expected)