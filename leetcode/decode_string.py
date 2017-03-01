class Solution(object):
  def decodeString(self, s, i = 0):
    """
    :type s: str
    :rtype: str
    """
    res = ""
    k = ""
    substring = ""


  def get_inner(self, s, i = 0):
    start = i
    prefix = ""
    while i < len(s) and s[i].isalpha():
      prefix += s[i]
      i += 1
    k = ""

    while i < len(s) and s[i].isdigit():
      k += s[i]
      i += 1

    res = ""
    i += 1        # skip [
    while i < len(s) and s[i] != "]":
      if s[i].isdigit():
        hi, i = self.get_inner(s, i)
        res += hi
      else:
        res += s[i]
      i += 1
    if len(k):
      k = int(k)
      res = res * k
    print(s[start: i])
    if i < len(s) - 1:
      i += 1
      postfix, i = self.get_inner(s, i)
      res += postfix

    res = prefix + res

    return res, i

s = "h3[a2[b]]k"
print(Solution().get_inner(s))