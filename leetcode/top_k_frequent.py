def top_k_frequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    dict = {}
    output = []
    lowest = None
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:


            dict[num] += 1


    lowest = list(dict.keys())[0]
    for key in dict.keys():
        if len(output) < k:
            output.append(key)
            print(lowest, key, dict)
            if dict[key] < dict[lowest]:
                lowest = key
        elif dict[key] > dict[lowest]:
            output[output.index(lowest)] = key

            lowest = output[0]

            for index in range(len(output)):
                if dict[output[index]] < dict[lowest]:
                    lowest = output[index]

    return output

print(top_k_frequent([1,1,1,2,2,3], 2))