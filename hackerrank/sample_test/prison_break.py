import numpy as np

def prison1(n, m, h, v):
  gate = np.ones((n + 1, m + 1))
  for i in h:
    gate[i] = gate[i - 1] = gate[i - 1] + gate[i]
    # print(gate, '\n')

  for i in v:
    gate[:, i] = gate[:, i - 1] = gate[:, i] + gate[:, i - 1]
  # print(gate, '\n')
  return np.max(gate)

def prison(n, m, h, v):
  h.sort()
  v.sort()
  h_count = 1 if len(h) > 0 else 0
  v_count = 1 if len(v) > 0 else 0
  max_h_count = h_count
  max_v_count = v_count

  prv = h[0] if len(h) > 0 else 0
  for i in range(1, len(h)):
    if h[i] == prv + 1:
      h_count += 1
      max_h_count = max(max_h_count, h_count)
    else:
      h_count = 1
    prv = h[i]

  prv = v[0] if len(v) > 0 else 0
  for i in range(1, len(v)):
    if v[i] == prv + 1:
      v_count += 1
      max_v_count = max(max_v_count, v_count)
    else:
      v_count = 1
    prv = v[i]

  space = (1 + max_v_count) * (1 + max_h_count)
  return space

def test(n, m, h, v, expected):
  val = prison(n, m, h, v)
  print(val, expected)
  assert val == expected


def test1(n, m, h, v):
  print(prison(n, m, h, v), prison1(n, m, h, v))
  assert prison(n, m, h, v) == prison1(n, m, h, v)

# n = 3
# m = 3
# h = [2]
# v = [2]
# expected = 4
# test(n, m, h, v, expected)
#
# n = 3
# m = 2
# h = [1, 2, 3]
# v = [1, 2]
# expected = 12
# test(n, m, h, v, expected)
#
# n = 5
# m = 5
# h = [1, 3, 2]
# v = [1, 2]
# expected = 12
# test(n, m, h, v, expected)
#
# n = 2
# m = 2
# h = []
# v = []
# expected = 1
# test(n, m, h, v, expected)
#
# n = 4
# m = 4
# h = [1, 3]
# v = [1, 3]
# expected = 4
# test(n, m, h, v, expected)
#
# n = 4
# m = 4
# h = [1, 3]
# v = []
# expected = 2
# test(n, m, h, v, expected)
#
# n = 5
# m = 5
# h = [1, 2]
# v = [5]
# expected = 6
# test(n, m, h, v, expected)


#
# n = 20
# m = 10
# h = [1, 12, 3 ,15 ,6]
# v = [1, 3,5 ,8]
# test1(n, m, h, v)
# #
# n = 20
# m = 10
# h = [1, 2, 3]
# v = []
# test1(n, m, h, v)

s= "saveChangesInTheEditor"
cnt = 1 if len(s) > 0 else 0
for ch in s:
  if ch.isupper():
    cnt += 1
print(cnt)