class Solution(object):
    def minMoves2e(self, nums):
        res = [99999, -1]
        for index in range(min(nums), max(nums)):
            sum = 0
            for num in nums:
                sum += abs(index - num)
            print(index, sum)
            if sum < res[0]:
                res = [sum, index]
        return res

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num

        if (sum / len(nums)) % 1 > 0.5:
            average = int(sum / len(nums)) + 1
        else:
            average = int(sum / len(nums))
        moves = 0
        print(average, sum / len(nums) )
        for num in nums:
            moves += abs(num - average)
        return moves

print(Solution().minMoves2e([1,0,0,8,6]))