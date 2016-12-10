def parent(i):
    if i % 2 == 0:
        return int((i-1) / 2)
    return int(i / 2)


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def swap(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp


def heapify(arr, i):
    l = left_child(i)
    r = right_child(i)

    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r < len(arr) and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)


def build_heap(arr):
    for i in range(int((len(arr) / 2) - 1), -1, -1):
        heapify(arr, i)


def heap_sort(arr):
    build_heap(arr)
    for index in range(len(arr) - 1, 1, -1):
        swap(arr, 0, index)
        heapify(arr, 0)
    return arr

arr = [4, 16, 10, 14, 7, 9, 3, 2, 8, 1]
arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
# heapify(arr, 0)
# build_heap(arr)
print(heap_sort(arr))