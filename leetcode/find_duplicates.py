import numpy as np


class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1
            else:
                res.append(abs(num))
        return res

arr = [4,3,2,7,8,2,3,1]

print(Solution().findDuplicates(arr))