BASE = ord('0')

def isBeautiful(string, size=1, isFlexible=True):
  if len(string) == 1 and isFlexible:
    return False, ''

  first = int(string[:size])
  second = str(first + 1)

  nextNumIndex = size + len(second)
  if second == string[size:nextNumIndex]:
    if nextNumIndex < len(string):
      a, b = isBeautiful(string[size:], len(second), False)[0], first
      if a:
        return a, b
    else:
      return True, first

  if isFlexible and size < len(string):
    return isBeautiful(string, size + 1, True)

  return False, first

def test(string, isB, out=''):
  a, b = isBeautiful(string)
  assert a == isB
  if a and isB:
    assert b == out

test('99100101', True, 99)
test('565758596061', True, 56)

