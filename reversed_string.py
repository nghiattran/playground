def reverse_string(string):
    words = string.split(' ')
    res = ''
    for i in range(len(words)):
        res += words[len(words) - 1 - i]
        if i != len(words) - 1:
            res += ' '
    return res

def reverse_word(word):
    pass

string = 'Do or do not, there is no try.'
res = reverse_string(string)
print(res)