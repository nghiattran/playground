gcd_memory = {}
class Value():
    def __init__(self):
        self.value = None

def gcd(x, y):
    a = max(x, y)
    b = min(x, y)
    obj = Value()

    while b:
        a, b = b, a % b
        key = str(a) + '-' + str(b)
        if key in gcd_memory:
            return gcd_memory[key].value
        gcd_memory[key] = obj

    obj.value = a
    return a

memory = {}
def maximumGcdAndSum(A, B):
    largest = -float("inf")
    A.sort()
    x = A[0]
    for y in B[-10:]:
        d = gcd(y, x)
        largest = max(d, largest)
        if d == largest:
            if d not in memory:
                memory[d] = (x, y)
            elif sum(memory[d]) < sum([x, y]):
                memory[d] = (x, y)
    return sum(memory[largest])

import random
import time
n = int(5*1e5)
m = int(5*1e6)
s = int(1e5)

A = [random.randrange(s, m) for _ in range(n)]
B = [random.randrange(s, m) for _ in range(n)]


start = time.time()
print(maximumGcdAndSum(A, B))
print(time.time() - start)