def count_negative(arr):
    row = 0
    column = len(arr[0]) -1
    count = 0

    while row < len(arr) and column >= 0:
        if arr[row][column] < 0:
            count += column + 1
            row +=1
            if column != len(arr[0]) -1:
                column -= 1
        else:
            column -= 1
    return count

arr =[
    [-11, -8, -6, -5],
    [-4, -3, -2, -2],
    [-3, -2, -1, 1],
    [-2, 2, 3, 4],
    [4, 5, 7, 8]
]

print(count_negative(arr))
