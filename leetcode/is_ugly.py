def isUgly(num):
    arr = [2, 3, 5]

    print(num)
    if num == 1 or num == -1:
        return True

    for divisor in arr:
        if num % divisor == 0:
            return isUgly(num / divisor)
    return False

print(isUgly(-2147483648))