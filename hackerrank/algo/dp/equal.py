def equalize(candies):
  pass

def test(candies, expected):
  res = equalize(candies)
  assert res == expected

cans = [2, 2, 3, 7]

print(equalize(cans))