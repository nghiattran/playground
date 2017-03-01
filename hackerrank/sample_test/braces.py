def braces(values):
  queue = []
  for ch in values:
    if ch == '{' or ch == '(' or ch == '[':
      queue.append(ch)
    else:
      if len(queue) == 0:
        return False

      open = queue.pop()
      if (open == '{' and ch !='}') or (open == '[' and ch !=']') \
        or (open =='(' and ch !=')'):
        return False
  return len(queue) == 0

def test(val, exp):
  res = braces(val)
  assert exp == res

s = '{}[]()'
braces(s)

s = '{}[]()'
test(s, True)

s = '{[]()}'
test(s, True)

s = '{[}]'
test(s, False)

s = '{[}]}'
test(s, False)

s = '{[}}'
test(s, False)

s = '{['
test(s, False)

s = '}'
test(s, False)