def isLucky(x):
    arr_x = [int(char) for char in str(x)]
    return sum(arr_x[:3]) == sum(arr_x[-3:])

last = -1
diff = 1e6
cnt = 0
for num in range(int(1e6), int(1e7)):
    if isLucky(num):
        if last == -1:
            last = num
        else:
            diff = min(num - last, diff)
        cnt += 1

print(diff)
print(cnt)
print(1e6 - 1e5)
