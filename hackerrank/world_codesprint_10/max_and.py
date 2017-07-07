import itertools
import math


def solve(n, k, a):
    high = max(a)
    max_bits = len(bin(high)) - 2

    for i in range(0, max_bits + 1):
        signs = [[], []]

        for num in a:
            sign = (num & (1 << (max_bits - i))) !=  0
            signs[sign].append(num)
        if len(signs[1]) >= k:
            a = signs[1]

    and_val = a[0]
    for num in a[1:k]:
        and_val &= num

    cnt = math.factorial(len(a)) // (math.factorial(k)* math.factorial(len(a) - k)) % int((1e9 + 7))

    return '%d\n%d' % (and_val, cnt)



def test(i, k, o):
    res = solve(len(i), k, i)
    try:
        assert res == o
    except Exception as e:
        print('Expected', o, '. Got', res)


i = [3, 4, 6, 7]
k = 3
o = "4\n1"
test(i, k, o)

i = [3, 5, 6]
k = 2
o = "4\n1"
test(i, k, o)

i = [21, 19, 22, 20]
k = 2
o = "20\n3"
test(i, k, o)

i = [9, 15, 27, 14]
k = 3
o ="10\n1"
test(i, k, o)

i = [41, 36, 33]
k = 2
o ="33\n1"
test(i, k, o)

o = '144115188075855872\n518646137'
with open('input.txt', 'r') as f:
    content = f.read()
    i = [int(num) for num in content.split('\n')]
k = 38079
test(i, k, o)