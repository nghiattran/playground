def solve(arr):
  tmp = 0
  for i in arr:
    tmp ^= i
  return tmp

def test(arr, expected):
  res = solve(arr)
  print(res, expected)
  assert res == expected

arr = [1, 1, 2]
expected = 2
test(arr, expected)

arr = [1, 3, 4, 2, 3, 1, 4]
expected = 2
test(arr, expected)

def maxXor(l, r):
  max = 0
  for i1 in range(l, r + 1):
    for i2 in range(i1, r + 1):
      if i1 ^ i2 > max:
        max = i1 ^ i2
  return max

print(maxXor(5, 6))