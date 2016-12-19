def prettyPrint(num):
    size = (num - 1) * 2 + 1
    arr = [[0] * size for i  in range(size)]
    for i in range(num):
        for index in range(i, size - i):
            arr[index][i] = num
            arr[index][size - i - 1] = num

        for index in range(i, size - i):
            arr[i][index] = num
            arr[size - i - 1][index] = num
        num -= 1
    return arr

res = prettyPrint(4)

for arr in res:
    print(arr)