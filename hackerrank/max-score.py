import itertools

def getMaxScoreTidious(a, n):
    print(  )
    # a = sorted(a, reverse=True)[:n+]
    print(a)
    # Complete this function
    max_total_score = 0
    for com in itertools.permutations(a, n):
        running_sum = 0
        total_score = 0
        for i in com:
          total_score += running_sum % i
          running_sum += i
        # print(com, sum(com), total_score)
        if max_total_score <= total_score:
            max_total_score = total_score
            print(com, sum(com),total_score)
    return max_total_score

def getMaxScore(a, n):
    pass

def test(i, n, o):
    res = getMaxScoreTidious(i, n)
    assert res == o, 'Expected %s. Got %s' % (str(o), str(res))


# test([4, 8, 5], 3, 6)
# test([4, 8, 5, 1, 1], 3, 7)
test([3, 4, 5, 1, 2, 3, 4, 1, 89], 5, 23)
# test([4, 8, 9, 6, 45, 6, 3, 4, 6, 8, 15, 20], 5, 72)