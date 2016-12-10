a = 60
b = 13

def update_bits(first, second, i, j):
    max = ~0
    right = (1 << j) -1
    left = max - right
    mask = left | right

    return (first & mask) | (second << i)

def print_float(float_string):
    int_part, float_part = float_string.split('.')

    number = ''
    int_part = bin(int(int_part))

    return int_part

def check(n):
    print(bin(n - 1))
    print(bin(n))
    print(bin(n & (n - 1)))
    return ((n & (n - 1)) == 0)

# print(print_float('18.26'))

x = 8
# print(bin(x))
# print(bin(0xa))
# print(bin(x & 0xaaaaaa))
# print(bin((x & 0xaaaaaa) >> 1))


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        nums = []
        for num in range(3):
            if num in dict:
                nums.extend([num] * dict[num])
        print(nums)

print(Solution().sortColors([1,0]))