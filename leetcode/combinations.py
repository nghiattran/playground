class Solution(object):
  def combine(self, n, k, start = 1):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    if k == 1:
      return [[num] for num in range(start, n + 1)]

    res = []
    for num in range(start, n):
      coms = self.combine(n, k - 1, num + 1)
      for com in coms:
        res.append([num] + com)
    return res
n = 4
k = 3
print(Solution().combine(n, k))