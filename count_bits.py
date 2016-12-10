import math
# from math import log

def count(num):
    list = []
    for index in range(num + 1):
        if index == 0:
            list.append(0)
        else:
            bits = math.log(index, 2)
            if bits % 1 == 0:
                bits = int(bits) + 1
            else:
                bits = math.ceil(bits)
            # list.append(count_bit(index, bits))

            count = 0
            while bits != 0:
                count += int(((index) % pow(2, bits)) / pow(2, bits - 1))
                bits -= 1
            list.append(count)
    return list

def count_bit(num, bits):

    count = 0
    while bits != 0:
        count += int(((num) % pow(2, bits)) / pow(2, bits - 1))
        bits -= 1
    return count

def count_bit1(num):
    count = 0
    while num != 0:
        count += 1
        print('start')
        print(num, bin(num))
        print(bin(num - 1), bin(num & num - 1))
        num = num & num - 1
    return count

print(count(5))
print(count_bit1(5))