def lcs(first, second):
    m = len(first) + 1
    n = len(second) + 1
    c = [[0 for x in range(n)] for y in range(m)]
    b = [['0' for x in range(n)] for y in range(m)]

    for i in range(1, m):
        c[i][0] = 0
    for i in range(1, n):
        c[0][i] = 0

    for x in range(1, m):
        for y in range(1, n):

            if first[x - 1] == second[y - 1]:
                c[x][y] = c[x - 1][y -1] + 1
                b[x][y] = '↖'
            elif c[x - 1][ y] >= c[x][y - 1]:
                c[x][y] = c[x - 1][y]
                b[x][y] = '↑'
            else:
                c[x][y] = c[x][y - 1]
                b[x][y] = '←'

    return get_lcs(first, second, b)

def get_lcs(first, second, arr):

    x = len(arr) - 1
    y = len(arr[0]) - 1
    chars = []

    while (x != 0 and y != 0):
        if arr[x][y] == '↑':
            x -= 1
        elif arr[x][y] == '←':
            y -= 1
        else:
            x -= 1
            y -= 1
            chars.append(first[x])

    print_chart(arr, first, second)
    chars.reverse()
    return ''.join(chars)

def print_chart(arr, first, second):
    print('      ',[char for char in second])

    for index, row in enumerate(arr):
        print(first[index - 1], row)

def printout(arr):
    for row in arr:
        print(row)

first = 'bdcaba'
second = 'abcbdab'

print(lcs(second, first))