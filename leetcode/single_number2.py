class Solution(object):
  def singleNumber(self, nums):
    a = b = 0

    for c in nums:
      ta = (~a&b&c)|(a&~b&~c)
      b = (~a & ~b & c) | (~a & b & ~c)
      a = ta
    return a | b

arr = [1, 6, 1, 4, 3, 7, 3, 4, 3, 1, 4, 6, 7]
print(Solution().singleNumber(arr))

# current   incoming  next
# a b c           c    a b c
# 0 0 0           0    0 0 0
# 1 0 0           0    1 0 0
# 0 1 0           0    0 1 0
# 1 1 0           0    1 1 0
# 0 0 1           0    0 0 1
# 0 0 0           1    1 0 0
# 1 0 0           1    0 1 0
# 0 1 0           1    1 1 0
# 1 1 0           1    0 0 1
# 0 0 1           1    1 0 1

# current   incoming  next
# a b c           c    a b c
# 1 0 0           0    1 0 0
# 1 1 0           0    1 1 0
# 0 0 0           1    1 0 0
# 0 1 0           1    1 1 0
# 0 0 1           1    1 0 1

# a = a