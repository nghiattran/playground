def find(year):
  if year > 1918:
    day, moth = gregorian(year)
  elif year == 1918:
    day, moth = 26, 9
  else:
    day, moth = julian(year)
  return '%02d.%02d.%d' %(day, moth, year)


def julian(year):
  if year % 4 == 0:
    return 12, 9
  return 13, 9


def gregorian(year):
  if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    return 12, 9
  return 13, 9

def test(year, expected):
  res = find(year)
  print(res, expected)
  assert res == expected

year = 2017
expected = '13.09.2017'
test(year, expected)

year = 2016
expected = '12.09.2016'
test(year, expected)

year = 1800
expected = '12.09.1800'
test(year, expected)

year = 1801
expected = '13.09.1801'
test(year, expected)

year = 1918
expected = '26.09.1918'
test(year, expected)

year = 1917
expected = '13.09.1917'
test(year, expected)