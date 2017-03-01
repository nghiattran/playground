import random

import numpy as np

def game(a, b, sum):
  aDict = [0]
  for i in range(len(a)):
    if aDict[i] + a[i] > sum:
      break;
    aDict.append(aDict[i] + a[i])

  bDict = [0]
  for i in range(len(b)):
    if bDict[i] + b[i] > sum:
      break;
    bDict.append(bDict[i] + b[i])

  pA = 0
  pB = len(bDict) - 1
  max = pB
  while pA != len(aDict) or pB != 0:
    total = aDict[pA] + bDict[pB]

    if total <= sum and pA + pB > max:
      max = pA + pB

    if total > sum:
      if pB > 0:
        pB -= 1
      else:
        pA += 1
    else:
      if pA < len(aDict) - 1:
        pA += 1
      else:
        break
  return max

def game1(a, b, sum):
  aDict = [0]
  for i in range(len(a)):
    if aDict[i] + a[i] > sum:
      break;
    aDict.append(aDict[i] + a[i])

  bDict = [0]
  for i in range(len(b)):
    if bDict[i] + b[i] > sum:
      break;
    bDict.append(bDict[i] + b[i])

  max = 0
  for x in range(len(aDict)):
    for y in range(len(bDict)):
      if aDict[x] + bDict[y] <= sum and x + y > max:
        max = x + y
  return max


def test(a, b, sum, target):
  res1 = game1(a, b, sum)
  res2 = game(a, b, sum)
  if (res1 != res2): print('Error', res1, res2)
  assert res1 == res2

while True:
  a = np.random.randint(100, size=5)
  b = np.random.randint(100, size=5)
  sum = random.randint(50, 1000)

  print(a, '\n', b, '\n', sum)
  test(a, b, sum, 5)

# a = [69, 64, 60, 65, 28]
# b = [99, 62, 97, 34, 65]
# sum = 154
# test(a, b, sum, 4)


# a = [4, 2, 4, 6, 1]
# b = [2, 1, 8, 5]
# sum = 10
# test(a, b, sum, 4)

# a = [2, 3, 1, 4, 5]
# b = [5, 1, 1, 1, 1, 1, 1, 1]
# sum = 9
# test(a, b, sum, 5)

# a = [1, 1, 1]
# b = [1, 1, 1]
# sum = 9
# test(a, b, sum, 6)
#
# a = [1, 1, 1]
# b = [1, 1, 1]
# sum = 5
# test(a, b, sum, 5)
#
# a = [0, 0, 0, 0, 0, 0,]
# b = [1, 1, 1]
# sum = 5
# test(a, b, sum, 9)
#
# a = [4, 2, 4, 6, 1]
# b = [2, 4, 8, 5]
# sum = 16
# test(a, b, sum, 5)
#
#
# a = [6, 6, 1, 1, 1]
# b = [3, 3, 3, 9, 8]
# sum = 21
# test(a, b, sum, 7)
#
# a = [6, 6, 1, 1, 1, 56,5, 6, 6,56,5,6,56, 5,6]
# b = [3, 3, 3, 9, 8, 6, 9, 5, 26,8, 56, 3,65,4,6 ,56,5, 6,0]
# sum = 23
# test(a, b, sum, 7)

# a = b = [0] * int(1e5)
# sum = 1
# test(a, b, sum, 1e5 * 2)