class Solution(object):
  def combinationSum3(self, k, n, start=1):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    if k == 1:
      return [[n]] if start <= n <= 9 else []
    res = []
    for i in range(start, 10):
      if i > n:
        return res
      result = self.combinationSum3(k - 1, n - i, i + 1)
      if result is not None:
        for com in result:
          res.append([i] + com)
    return res

k = 3
n = 9
print(Solution().combinationSum3(k, n))