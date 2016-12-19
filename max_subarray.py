def maxset(arr):
    arr.append(-1)
    max = -1
    maxArr = []
    start = 0
    end = 0
    for index in range(len(arr)):
        print(arr[index])
        if arr[index] >= 0:
            end += 1
        elif start == end:
            end += 1
            start = end
        else:
            print(start, end, arr[start: end])
            if sum(arr[start: end]) > max:
                maxArr = arr[start: end]
                max = sum(maxArr)
            elif sum(arr[start: end]) == max and end - start > len(maxArr):
                maxArr = arr[start: end]
                max = sum(maxArr)
            end += 1
            start = end

    return maxArr

print(maxset([ -846930886, -1714636915, 424238335, -1649760492 ]))