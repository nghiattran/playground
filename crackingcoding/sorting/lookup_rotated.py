def lookup(arr, key, start = 0, end = None):
    if end == None:
        end = len(arr) - 1
    if start > end:
        return None

    middle = int((end + start) / 2)

    if arr[middle] == key:
        return middle

    if arr[middle] < arr[end]:
        if arr[middle] <= key and key <= arr[end]:
            return lookup(arr, key, middle + 1, end)
        else:
            return lookup(arr, key, start, middle - 1)
    else:
        if arr[start] <= key and key <= arr[middle]:
            return lookup(arr, key, start, middle - 1)
        else:
            return lookup(arr, key, middle + 1, end)


def lookup1(arr, key, start = 0, end = None):
    if end == None:
        end = len(arr) - 1
    while start <= end:
        middle = int((end + start) / 2)

        if arr[middle] == key:
            return middle
        elif arr[start] <= arr[middle]:
            if key > arr[middle]:
                start = middle + 1
            elif key >= arr[start]:
                end = middle - 1
            else:
                start = middle + 1
        elif key < arr[middle]:
            end = middle - 1
        elif key <= arr[end]:
            start = middle + 1
        else:
            end = middle -1
    return -1

arr = [6, 7, 8, 9, 1 ,2 ,3, 4, 5]
value = 1
print(lookup(arr, value))
print(lookup1(arr, value))