def swap(nums, first, second):
    nums[first] = nums[first] + nums[second]
    nums[second] = nums[first] - nums[second]
    nums[first] = nums[first] - nums[second]

def partition(nums, l, r):
    x = nums[r]
    i = l

    for j in range(1, r - 1):
        if nums[j] <= x:
            swap(nums, i, j)
            i += 1
    swap(nums, i, r)
    return i

def k_smallest(nums, l, r, k):
    if k > 0 and k <= r - l + 1:
        pos = partition(nums, l, r)
        print(pos, pos - l > k -1)
        if pos - l == k - 1:
            return nums[pos]
        if pos - l > k -1:
            return k_smallest(nums, l, pos - 1, k)
        return k_smallest(nums, pos + 1, r, k - pos + l + 1)
    return None

def find(nums, k):
    return k_smallest(nums, 0, len(nums) - 1, k)

print(find([7, 10, 4, 3, 20, 15], 2))

