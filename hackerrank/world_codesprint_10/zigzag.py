def minimumDeletions(a):
    if len(a) == 0 or len(a) == 1 or len(a) == 2:
        return 0

    cnt = 0
    sign = a[1] > a[0]
    for i in range(2, len(a)):
        current_sign = a[i] > a[i-1]

        if sign == current_sign:
            # print(a[i-2], a[i-1], a[i], sign, current_sign)
            cnt += 1
        else:
            sign = current_sign
    return cnt

def test(i, o):
    res = minimumDeletions(i)
    try:
        assert res == o
    except Exception as e:
        print('Expected', o, '. Got', res)

i = '80 87 85 82 89 95 100 99 98 96 93 90 97 92 91 94 88 84 83 77 81 86 79 75 76 74 78 73 72 71 67 69 63 66 65 60 64 70 68 61 58 62 59 57 56 55 52 54 50 53 47 51 48 45 37 43 36 17 23 40 30 35 25 16 15 12 1 10 14 27 34 22 26 39 49 38 32 24 21 29 28 41 46 44 42 33 18 7 8 13 4 5 6 11 19 31 20 9 3 2'

test([int(x) for x in i.split(' ')], 53)
test([4, 2, 6, 3, 10, 1], 0)
test([5, 2, 3, 6, 1], 1)