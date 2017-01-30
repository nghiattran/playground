import numpy as np

import heapq

class Solution(object):
  def frequencySort(self, s):
    """
    :type s: str
    :rtype: str
    """
    h = []
    chs = {}
    for ch in s:
      if ch in chs:
        chs[ch] += 1
      else:
        chs[ch] = 1

    for key in chs:
      heapq.heappush(h, (chs[key], key))
      
    res = ''
    while len(h) != 0:
      fre, key = heapq.heappop(h)
      res = key * fre + res
    return res

string = "Aabb"
print(Solution().frequencySort(string))