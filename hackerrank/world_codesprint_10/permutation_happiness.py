import itertools

global_dict = {}
def query1(n, k):
    # Complete this function
    n = [i + 1 for i in range(n)]
    cnt = 0
    val_dict = {}
    for com in itertools.permutations(n, len(n)):
        happy_cnt = 0
        for i in range(0, len(com)):
            if i == 0:
                happy_cnt += com[i] < com[i + 1]
            elif i == len(com) - 1:
                happy_cnt += com[i] < com[i - 1]
            else:
                happy_cnt += com[i] < com[i-1] or com[i] < com[i + 1]
        # print(com, happy_cnt)
        val_dict[happy_cnt] = val_dict[happy_cnt] +1 if happy_cnt in val_dict else 1
        if happy_cnt >= k:
            cnt += 1

    print(len(n), end='--   ')
    for key in sorted(val_dict.keys()):
        print('%d: %d, ' % (key, val_dict[key]), end='')
    print()

    res = cnt
    return res % int(1e9 + 7)

def subquery(n):
    if n == 2:
        return {1: 2}

    res = subquery(n-1)

    for i in range(n):
        pass



def query(n, k):
    res = 0
    return res % int(1e9 + 7)


def test(i, k, o):
    res = query(i, k)
    try:
        assert res == o
    except Exception as e:
        print('Expected', o, '. Got', res)
        pass

query1(2, 1)
query1(3, 1)
query1(4, 1)
query1(5, 1)
query1(6, 1)
query1(7, 1)
query1(8, 1)
query1(9, 1)
# test(3, 2, 4)
# test(4, 3, 8)
# test(10, 7, 1433856)