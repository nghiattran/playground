def permutation(arr, res = ''):
    if type(arr) is str:
        arr = [char for char in arr]

    if len(arr) == 0:
        print(res)
        return

    for i in range(len(arr)):
        permutation([arr[index] for index in range(len(arr)) if i != index], res + arr[i])

