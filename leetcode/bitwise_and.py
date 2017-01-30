class Solution(object):
  def rangeBitwiseAnd(self, m, n):
    if m == 0:
      return 0
    print bin(m & n), m & n
    res = m
    for i in xrange(m + 1, n + 1):
      res &= i
    return res

first, second = 5, 7
print(bin(first), bin(second))
print(Solution().rangeBitwiseAnd(first, second))