def search(nums, value, start, end):
    if start > end:
        return -1

    mid = int((end + start) / 2)

    if nums[mid] == value:
        return mid
    elif nums[mid] > value:
        return search(nums, value, start, mid - 1)
    else:
        return search(nums, value, mid + 1, end)

def k_closet(nums, value ,k):
    output = []
    index = search(nums, value, 0, len(nums) - 1)

    if index == -1:
        return output

    right = index + 1
    left = index - 1
    for i in range(k):
        if right >= len(nums) or nums[right] - value > value - nums[left]:
            output.append(nums[left])
            left -= 1
        elif left < 0 or value - nums[left] > nums[right] - value:
            output.append(nums[right])
            right += 1
    return output

print(k_closet([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 35, 4))