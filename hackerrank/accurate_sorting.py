def is_sortable(n):
    l = dict(zip(n, range(len(n))))
    sl = dict(zip(sorted(n), range(len(n))))

    for k in l.keys():
        if abs(l[k] - sl[k]) > 1:
            return 'No'

    return 'Yes'

def test(i, o):
    res = is_sortable(i)
    try:
        assert res == o
    except Exception as e:
        print('Expected', o, '. Got', res)


test([1, 0, 3, 2], 'Yes')
test([2, 1, 0], 'No')
# test('abab', 3)
# test('acbdabcd', 12)
# test('aacdbb', 6)