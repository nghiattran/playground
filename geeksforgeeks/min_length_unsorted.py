def min_length_unsorted(nums):
    lowbound = -1
    highbound = -1

    for index in range(1,len(nums)):
        if nums[index] < nums[index-1] and (lowbound == -1 or lowbound > index - 1):
            lowbound = index - 1

    for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1] and (highbound == -1 or highbound < index + 1):
            highbound = index + 1

    min_value = min(nums[lowbound: highbound + 1])
    max_value = max(nums[lowbound: highbound + 1])

    index = lowbound
    while index > 0:
        if nums[index - 1] > min_value:
            lowbound = index - 1
        index -= 1

    index = highbound
    while index < len(nums) - 1:
        if nums[index + 1] < max_value:
            highbound = index + 1
        index += 1

    return lowbound, highbound

print(min_length_unsorted([0, 1, 15, 25, 6, 7, 30, 40, 50]))