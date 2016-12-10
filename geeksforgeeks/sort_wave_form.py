def sort_wave_form(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        last = len(nums) - 1
    else:
        last = len(nums) - 2

    pointer = 0
    while pointer < last:
        swap(nums, pointer, last)
        pointer += 2
        last -= 2
    return nums

def swap(nums, first, second):
    nums[first] = nums[first] + nums[second]
    nums[second] = nums[first] - nums[second]
    nums[first] = nums[first] - nums[second]

def sort_wave_form1(nums):
    for index in range(0, len(nums), 2):
        if index > 0 and nums[index] < nums[index - 1]:
            swap(nums, index, index - 1)

        if index + 1 < len(nums) - 1 and nums[index] > nums[index + 1]:
            swap(nums, index, index + 1)
    return nums


print(sort_wave_form1([10, 5, 6, 3, 2, 20, 100, 80]))