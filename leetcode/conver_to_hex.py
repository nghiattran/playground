import math


class Solution(object):
  def toHex(self, num):
    """
    :type num: int
    :rtype: str
    """
    ceil = 0x100000000
    if num < 0:
      num = ceil + num
    if num == 0: return "0"

    res = ""
    base = ord('a')
    base_num = ord('0')

    while num > 0:
      val = num & 15
      if val >= 10:
        val = val - 10 + base
      else:
        val = val + base_num
      res = res + chr(val)
      num = num >> 4

    return res

val = -1

print(Solution().toHex(val))