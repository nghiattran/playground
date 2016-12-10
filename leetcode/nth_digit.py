import math

def nth_digit(num):
    if num <= 9:
        return num

    base = 9
    digit = 1
    while base < num:
        base *= 10
        digit += 1
    base /= 10

    num -= base + 1
    index = num % digit
    num = int(math.ceil(num / digit))
    num = base + num
    return str(num)[int(index)]

print(nth_digit(10))
print(nth_digit(3))