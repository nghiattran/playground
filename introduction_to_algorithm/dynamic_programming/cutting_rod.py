# Approach one: using brute-force recursive.
# CUT-ROD.p; n/
# 1 if n == 0
# 2     return 0
# 3 q = -1
# 4 for i = 1 to n
# 5     q = max(q, pi + CUT-ROD(p, n - i))
# 6 return q

def find_optimal(length, prices):
    return cut_rod(length, prices)


def cut_rod(n, prices):
    if n == 0:
        return 0
    q = 0
    for i in range(1, n):
        q = max(q, prices[i - 1] + cut_rod(n - i, prices))
    return q

prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print(find_optimal(10, prices))