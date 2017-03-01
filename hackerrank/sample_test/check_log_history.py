

def check_log_history(events):
  queue = []
  acc = {}

  for i in range(len(events)):
    e = events[i]
    opt, val = e.split(' ')
    if opt == 'ACQUIRE':
      if val in acc:
        return i + 1

      acc[val] = True
      queue.append(val)
    else:
      if len(queue) == 0:
        return i + 1
      open = queue.pop()
      if open != val:
        return i + 1
      del acc[val]
  return 0 if len(queue) == 0 else len(events) + 1

events = [
  'ACQUIRE 364',
  'ACQUIRE 84',
  'RELEASE 84',
  'RELEASE 364'
]
print(check_log_history(events))

events = [
  'ACQUIRE 364',
  'ACQUIRE 84',
  'RELEASE 364',
  'RELEASE 84'
]
print(check_log_history(events))

events = [
  'ACQUIRE 123',
  'ACQUIRE 84',
  'RELEASE 364',
  'RELEASE 84'
]
print(check_log_history(events))

events = [
  'ACQUIRE 364',
  'ACQUIRE 84',
  'RELEASE 364',
  'RELEASE 84'
]
print(check_log_history(events))

events = [
  'ACQUIRE 364',
  'ACQUIRE 84',
  'RELEASE 364',
  'RELEASE 84'
]
print(check_log_history(events))