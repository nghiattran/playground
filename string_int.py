def string_to_int(string):
    sign = -1 if string[0] == '-' else 1
    integer = 0
    base = 1
    for i in range(len(string) -1, -1, -1):
        if string[i] != '-':
            integer += (ord(string[i]) - 48) * base
        base *= 10
    return integer * sign

def int_to_string(num):
    sign = '-' if num < 0 else ''
    string = ''
    num = abs(num)
    while num > 0:
        string = chr(num % 10 + 48) + string
        num = int(num / 10)
    return sign + string

string = '-6513'
integer = string_to_int(string)
print(integer, type(integer))

string = int_to_string(integer)
print(string, type(string))