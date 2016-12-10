def productExceptSelf(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0, n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output

def productExceptSelf1(nums):
    product = 1
    output = []

    for num in nums:
        output.append(product)
        product *= num
    product = 1

    for index in range(len(nums) - 1, -1, -1):
        output[index] *= product
        product *= nums[index]
    return output

arr = [2, 3, 5, 6]
print(productExceptSelf1(arr) == productExceptSelf(arr))