def count_substring_length(string, length):
    dict = {}
    for index in range(len(string) - length + 1):
        if string[index : index + length] not in dict:
            dict[string[index : index + length]] = None
    return len(dict)

def count_distinct_substring(string):
    count = 1
    for length in range(1, len(string) + 1):
        count += count_substring_length(string, length)
    return count

print(count_distinct_substring("ababa"))