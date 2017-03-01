unsorted = [1, 1, 3, 10, 3, 5]
sort = [0] * int(1e7)
print(type(sort))
for num in unsorted:
  sort[num] += 1

for i in range(len(sort)):
  if sort[i] > 0:
    print(('%d\n' % (i + 1)) * sort[i])
