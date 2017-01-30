class Solution(object):
  def combinationSum(self, candidates, target, start = 0, dic={}):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    length = len(candidates)
    if length == 0:
      return [[]]

    res = []
    for i in range(start, length):
      if candidates[i] > target:
        continue
      elif candidates[i] == target:
        res.append([candidates[i]])
        continue

      coms = self.combinationSum(candidates, target - candidates[i], i)
      for com in coms:
        res.append([candidates[i]] + com)

    return res


candidates = [2,3,6,7]
target = 7
print(Solution().combinationSum(candidates, target))