def isPower(num):
    return num & (num-1) == 0

print(isPower(16))

