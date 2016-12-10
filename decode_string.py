def decode(string):
    num = ''
    phrase = ''
    res = ''
    state = -1
    for char in string:
        if state == -1:
            if char.isdigit():
                state = 0
            else:
                res += char
        elif state == 0:
            if char == '[':
                state = 1
            else:
                num += char
        else:
            if char == ']':
                for index in range(int(num)):
                    res += phrase

                num = ''
                phrase = ''
                state = 0
            else:
                phrase += char
    return res

print(decode("3[a2[c]]"))