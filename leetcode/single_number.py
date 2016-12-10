class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = 0
        b = 0
        for num in nums:
            xor ^= num
            print(bin(xor), bin(num))
        print(bin(xor))
        mask = 1
        while(xor&mask == 0):
            mask = mask << 1
        print('mask', bin(mask))
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]

print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))