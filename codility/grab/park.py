import math

def parse_time(t):
    t = [int(num) for num in t.split(':')]
    return t[0] + t[1] * 0.01

def solution(E, L):
    # write your code in Python 2.7
    E = parse_time(E)
    L = parse_time(L)
    duration = math.ceil(L - E)
    return int(2 + 3 * 1 + (duration - 1) * 4)

print(solution('10:00', '13:21'))
print(solution('10:45', '11:46'))
print(solution('09:42', '11:42'))