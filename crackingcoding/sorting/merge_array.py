def merge(arr1, arr2):
    last = len(arr1) - 1
    last_arr1 = len(arr1) - len(arr2) - 1
    last_arr2 = len(arr2) - 1

    for index in range(0, last):
        if arr1[last_arr1] > arr2[last_arr2]:
            arr1[last] = arr1[last_arr1]
            last_arr1 -= 1
        else:
            arr1[last] = arr2[last_arr2]
            last_arr2 -= 1
        last -= 1
        if last_arr1 == last:
            break
    return arr1

print(merge([1, 2 , 4, 7, None, None], [2, 5 ,9]))