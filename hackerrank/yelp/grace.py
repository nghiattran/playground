import random

def merge_sorted_businesses(trendy_businesses, favorite_businesses):
    """
    Merges two already sorted lists of businesses (sorted based on number of reviews)
    and returns a sorted list of all businesses in descending order based on
    number of reviews.

    Args:
        trendy_businesses: Sorted list of dictionaries containing business_id and num_reviews.
        favorite_businesses: Sorted list of dictionaries containing business_id and num_reviews.

    Input:
    # trendy_businesses:
    [
        {'business_id': 100, 'num_reviews': 1000},
        {'business_id': 103, 'num_reviews': 900},
    ]
    # favorite_businesses:
    [
        {'business_id': 203, 'num_reviews': 950},
        {'business_id': 201, 'num_reviews': 800},
        {'business_id': 202, 'num_reviews': 700},
    ]
    Expected Output:
    [
        {'business_id': 100, 'num_reviews': 1000},
        {'business_id': 203, 'num_reviews': 950},
        {'business_id': 103, 'num_reviews': 900},
        {'business_id': 201, 'num_reviews': 800},
        {'business_id': 202, 'num_reviews': 700},
    ]
    """
    ## TODO: COMPLETE ME
    res = []
    trendy_businesses_pointer = 0
    favorite_businesses_pointer = 0

    while trendy_businesses_pointer < len(trendy_businesses) and favorite_businesses_pointer < len(favorite_businesses):
        if trendy_businesses[trendy_businesses_pointer]['num_reviews'] > \
            favorite_businesses[favorite_businesses_pointer]['num_reviews']:
            res.append(trendy_businesses[trendy_businesses_pointer])
            trendy_businesses_pointer += 1
        else:
            res.append(favorite_businesses[favorite_businesses_pointer])
            favorite_businesses_pointer += 1

    if trendy_businesses_pointer < len(trendy_businesses):
        res += trendy_businesses[trendy_businesses_pointer:]
    else:
        res += favorite_businesses[favorite_businesses_pointer:]
    return res

a = [{'num_reviews': 100000 - i} for i in range(10000)]
b = [{'num_reviews': 100000 - i} for i in range(100000)]

res = merge_sorted_businesses(a, b)

assert len(res) == len(a) + len(b)

for i in range(len(res) - 1):
    assert res[i]['num_reviews'] >= res[i+1]['num_reviews'], '%d %d' % (res[i]['num_reviews'], res[i+1]['num_reviews'])