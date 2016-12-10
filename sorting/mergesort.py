def mergesort(arr, start, end):
    if start < end:
        pivot = int((start + end) / 2)
        mergesort(arr, start, pivot)
        mergesort(arr, pivot + 1, end)
        merge(arr, start, pivot, end)

def merge(arr, start, pivot, end):
    i = j = 0
    L = arr[start:pivot]
    L.append(9999)
    R = arr[pivot:end]
    R.append(9999)
    for index in range(start, end):
        if L[i] <= R[j]:
            arr[index] = L[i]
            i += 1
        else:
            arr[index] = R[j]
            j += 1

arr = [0, 2, 2, 3, 5, 0, 1, 3, 4, 6]

mergesort(arr, 0, 10)
print(arr)