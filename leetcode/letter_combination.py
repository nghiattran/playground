class Solution(object):
  def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
            # 2      3        4     5      6     7         8
    list = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    char_list = ""
    res = []
    for i in digits:
      index = int(i) - 2
      print(index)
      char_list += list[index]

      if (len(res) == 0):
        res = [ch for ch in list[index]]
        continue

      tmp = []
      for ch in list[index]:
        for str in res:
          tmp.append(str + ch)
      res = tmp
    return res

digits= "23"
print(Solution().letterCombinations(digits))