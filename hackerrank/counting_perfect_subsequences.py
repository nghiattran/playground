def countSubs(s):
    sum = 0
    dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }



    return sum

def test(i, o):
    res = countSubs(i)
    try:
        assert res == o
    except Exception as e:
        print('Expected', o, '. Got', res)


test('abcd', 3)
test('cad', 1)
test('dcc', 2)
# test('abab', 3)
# test('acbdabcd', 12)
# test('aacdbb', 6)