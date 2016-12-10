def sort_anagram(arr):
    dict = {}
    for string in arr:
        for char in string:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
    char_list = list(dict.keys())
    char_list.sort()

    res = ''
    for char in char_list:
        res += char * char_list[char]
    return res

print(sort_anagram(['hello', 'what the fuck']))