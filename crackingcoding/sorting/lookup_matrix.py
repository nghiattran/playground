def get_coordinate(matrix, index):
    return [
        int(index / len(matrix)),
        index % len(matrix[0])
    ]


def get_value(matrix, index):
    coords = get_coordinate(matrix, index)
    return matrix[coords[0]][coords[1]]


def search(matrix, key):
    row = 0
    col = len(matrix[0]) - 1
    count = 0
    while row < len(matrix) and  col >= 0:
        count += 1
        print(count, row, col, matrix[row][col])
        if matrix[row][col] == key:
            return [row, col]
        elif matrix[row][col] > key:
            col -= 1
        else:
            row += 1

matrix = [
    [1, 2, 3],
    [4, 7 , 10],
    [5, 9, 12],
    [6, 11, 15],
    [8, 13, 17]
]

print(search(matrix, 11))