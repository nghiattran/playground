class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = 2 if k % 2 == 0 else 1
        print(k)
        for index in range(min(k, len(nums))):
            first = index
            second = (first + k) % len(nums)
            print(first, second, nums)
            nums[first], nums[second] = self.swap(nums[first], nums[second])
            while second != first:
                second = (second + k) % len(nums)
                print(first, second, nums)
                nums[first], nums[second] = self.swap(nums[first], nums[second])
        print(nums)


    def swap(self, first, second):
        first = first + second
        second = first - second
        first = first - second
        return first, second

print(Solution().rotate([1, 2, 3],  2))