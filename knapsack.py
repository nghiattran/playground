import time


def knapSack(val, wt, W, n):
    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n - 1] > W):
        return knapSack(val, wt, W, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(val, wt, W-wt[n-1], n-1),
                   knapSack(val, wt, W, n - 1))

def knapsack_bruteforce(values, weights, capacity, n = 0):
    max_value = 0

    for index in range(0, len(values)):
        if capacity >= weights[index]:
            tmp = knapsack_bruteforce(values[1:], weights[1:], capacity - weights[index])
            tmp_max_value = tmp + values[index]
            max_value = max(max_value, tmp_max_value)
    return max_value


def knapSack1(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 0

start = time.time()
for index in range(0, 1000000):
    knapsack_bruteforce(values, weights, capacity, len(values))
end = time.time()

print(end - start)

start = time.time()
for index in range(0, 1000000):
    knapSack(values, weights, capacity, len(values))

end = time.time()
print(end - start)

start = time.time()
for index in range(0, 1000000):
    knapSack1(val=values, wt=weights, W=capacity, n=len(values))

end = time.time()
print(end - start)