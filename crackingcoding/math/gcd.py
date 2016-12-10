def gcd(first, second):
    if second == 0:
        return first
    first = first % second
    return gcd(second, first)

print(270 * 192 / gcd(270, 192))

print(8640 / 270)
print(8640 / 192)
