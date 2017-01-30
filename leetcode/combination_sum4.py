class Solution(object):
  def combinationSum4(self, nums, target, dict = None):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    nums.sort()
    sums = [0] + [0] * target

    for i in range(target + 1):
      for num in nums:
        if num == i:
          sums[i] += 1
        elif num < target:
          sums[i] += sums[i - num]
        else:
          break
    return sums[target]

  # def combinationSum4(self, nums, target):
  #   nums.sort()
  #
  #
  #   pass

nums = [4,2,1]
target = 32
print(Solution().combinationSum4(nums, target))