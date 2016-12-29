class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pointer = None
        for i in range(len(nums) - 1, -1, -1):
            print(nums[i] != val)
            if nums[i] != val and pointer is None:
                pointer = i
            elif nums[i] == val and pointer is not None:
                nums[i] = nums[pointer] + nums[i]
                nums[pointer] = nums[i] - nums[pointer]
                nums[i] = nums[i] - nums[pointer]
                pointer -= 1
        return pointer + 1 if pointer is not None else len(nums)

print(Solution().removeElement([3,2,2,3],3))