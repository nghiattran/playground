def missingNumber(nums):
    missing = 0
    for index in range(0, len(nums)):
        missing += index - nums[index]
    return missing + len(nums)

def missingNumber1(nums):
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    for index in range(len(nums)):
        if index not in dict:
            return index
    return index + 1

print(missingNumber([0, 1]))
print(missingNumber([0, 1, 3]))
print(missingNumber([0]))
print(missingNumber([1]))

# print(missingNumber1([0, 1]))