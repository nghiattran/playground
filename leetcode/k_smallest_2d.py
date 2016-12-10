import heapq
def k_smallest(matrix, k):
    result, heap = None, []
    heapq.heappush(heap, (matrix[0][0], 0, 0))
    while k > 0:
        result, i, j = heapq.heappop(heap)
        print(result, i, j, heap)
        if i == 0 and j + 1 < len(matrix):
            heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        if i + 1 < len(matrix):
            heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
        k -= 1
    return result

matrix = [
    [1, 2, 8],
    [3, 5, 10],
    [6, 7, 12]
]

print(k_smallest(matrix, 7))