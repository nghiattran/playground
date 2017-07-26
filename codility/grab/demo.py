def solution(A):
    # write your code in Python 2.7
    total = 0
    sum_arr = []
    for i in range(len(A)):
        total += A[i]
        sum_arr.append(total)

    if sum_arr[-1] - sum_arr[0] == 0:
        return 0
    if sum_arr[-2] == 0:
        return len(A) - 1

    for i in range(1, len(A) - 1):
        if sum_arr[i - 1] == sum_arr[-1] - sum_arr[i]:
            return i

    return -1

print(solution([-1, 3, -4, 5, 1, -6, 2, 1]))
print(solution([1, -1, 1, -1, 1, -1]))
print(solution([-2147483648]))
print(solution( [500, 1, -2, -1, 2]))