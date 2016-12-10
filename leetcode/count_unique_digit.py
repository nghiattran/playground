def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 9 + countNumbersWithUniqueDigits(n - 1)

    output = 9
    multi = output
    count = n
    tmpoutput = output
    while count > 1:
        tmpoutput *= multi
        multi -= 1
        count -= 1
        output += tmpoutput
    return output + 1

print(countNumbersWithUniqueDigits(2))
