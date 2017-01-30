class Solution(object):
  def combinationSum2(self, candidates, target, start=0, dic={}):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if start == 0:
      candidates.sort()

    length = len(candidates)
    if length == 0 or str(candidates[start - 1]) + '-' + str(target) in dic:
      return [[]]
    res = []
    for i in range(start, length):
      if candidates[i] > target:
        continue
      elif candidates[i] == target:
        res.append([candidates[i]])
        continue

      coms = self.combinationSum2(candidates, target - candidates[i], i + 1,
                                  dic)
      for com in coms:
        res.append([candidates[i]] + com)
    return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))