import time

class Solution(object):
  def findTargetSumWays(self, nums, S, index = 0, dic = {}):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    key = '{0}-{1}'.format(S, index)

    if key in dic:
      return dic[key]

    num = nums[index]

    if len(nums) - 1 == index:
      if num == 0 and S == 0: return 2
      return 1 if num == abs(S) else 0

    dic[key] = (self.findTargetSumWays(nums, S - num, index + 1, dic) + \
     self.findTargetSumWays(nums, S + num, index + 1, dic))
    return dic[key]


class Solution1(object):
  def findTargetSumWays(self, nums, S):
    if not nums:
      return 0
    dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
    for i in range(1, len(nums)):
      tdic = {}
      for d in dic:
        tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
        tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
      dic = tdic
    return dic.get(S, 0)

nums, S = [1] * 50, 1

tic = time.time()
print(Solution().findTargetSumWays(nums, S))
toc = time.time()
print(toc - tic)

tic = time.time()
print(Solution1().findTargetSumWays(nums, S))
toc = time.time()
print(toc - tic)