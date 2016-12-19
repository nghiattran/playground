def num_of_one(num):
    count = 0
    while num != 0:
        if num & 1 == 1:
            count += 1
        num = num >> 1
    return count

num = 641323
print(bin(641323))
print(num_of_one(num))