def choose(A):
    if len(A) == 0:
        return 0

    # if buy 1 day ticket
    cost1 = choose(A[1:]) + 2

    # if buy 7 ticket
    start_date = A[0]
    i = 1
    while i < len(A) and A[i] <= start_date + 6:
        i += 1
    cost7 = choose(A[i:]) + 7

    return min(cost1, cost7)

def solution(A):
    # worst-case 30^2
    return min(25, choose(list(A)))

def test(arr, expect):
    assert solution(arr) == expect



arr = [1, 2, 4, 5, 7, 29, 30]
test(arr, 11)

arr = [1, 2, 3, 7, 9, 11, 14, 15, 16, 17]
test(arr, 16)

arr = []
test(arr, 0)

arr = [1]
test(arr, 2)

arr = [1, 2]
test(arr, 4)

arr = [1, 2, 3, 4, 5, 6, 7]
test(arr, 7)

arr = [num for num in range(24)]
test(arr, 25)

arr = [1, 5, 11, 14, 18, 26, 30]
test(arr, 14)