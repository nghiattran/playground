import math

def radixSort(a, base = 10):
    for x in range(int(math.ceil(math.log(max(a), base))) + 1):
        bins = [[] for i in range(base)]
        for y in a:
            bins[(y/10**x)%base].append(y)
        a=[]
        for section in bins:
            a.extend(section)
    return a

random_data = [40, 12, 45, 32, 33, 1, 22]
print(radixSort(random_data))