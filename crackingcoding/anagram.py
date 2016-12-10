def is_anagram(first, second):
    dict = {}
    for char in first:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    for char in second:
        if char in dict and dict[char] > 0:
            dict[char] -= 1
        else:
            return False
    return True

print(is_anagram('listen', 'silenta'))