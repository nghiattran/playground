def StairCase(n):
    for row in range(n):
        for col in range(n):
            if col >= n - 1 - row:
                print('#', end='')
            else:
                print(' ', end='')
        print()

StairCase(6)