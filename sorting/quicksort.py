def partition1(arr, start, end):
    last = arr[end]
    i = start - 1
    for index in range(start, end):
        if arr[index] <= last:
            i += 1
            swap(arr, index, i)
    swap(arr, i + 1, end)
    return i

def partition2(arr, start, end):
    pivot = arr[start]
    i = start - 1
    j = end + 1

    while True:
        j -= 1

        while arr[j] > pivot:
            j -= j

        i +=1

        while arr[i] < pivot:
            i += 1

        if i < j:
            swap(arr, i, j)
        else:
            return j

def swap(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp

def quicksort(arr, start, end):
    if start < end:
        split = partition2(arr, start, end)
        # quicksort(arr, start, split)
        # quicksort(arr, split + 1, end)

arr = [2, 8, 7, 1, 3, 5, 6, 4]
index = quicksort(arr, 0, 7)
print(arr)