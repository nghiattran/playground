class Solution(object):
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n == 4:
      return False

    square_sum = 0
    while n != 0:
      square_sum += (n % 10) ** 2
      n /= 10

    if square_sum == 1:
      return True

    return self.isHappy(square_sum)

print(Solution().isHappy(200654))