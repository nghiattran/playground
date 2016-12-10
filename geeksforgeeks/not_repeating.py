def strange_clock(t):
    threshold = 3
    start = 1
    while (t - start) / threshold > 1:
        start += threshold
        threshold *= 2

    index = t - start
    return threshold - index

print(strange_clock(21))
