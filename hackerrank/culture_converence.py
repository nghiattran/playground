class Node():
    def __init__(self, val, sup, is_burnt=False):
        self.val = val
        self.sup = sup
        self.sub = []
        self.is_burnt = is_burnt
        self.ad = 1 if is_burnt else 0
        if sup:
            self.sup.sub.append(self)

    def reset(self):
        self.ad = 0
        self.is_burnt = False

    def count(self):
        self.ad = 0
        subsub = 0
        if self.sup and self.sup.is_burnt == True:
            self.ad += 1

            if self.sup.sup and self.sup.sup.is_burnt == True:
                subsub += 1

        for sub in self.sub:
            if sub.is_burnt == True:
                self.ad += 1

                for s in sub.sub:
                    if s.is_burnt or subsub:
                        subsub += 1

        if subsub > 0:
            self.ad = max(0.8, self.ad - subsub * 0.0001)

def send(node):
    node.reset()
    if node.sup:
        node.sup.reset()

    for em in node.sub:
        em.reset()

def make_dict(dict, n):
    if n.ad > 0:
        if n.ad in dict:
            dict[n.ad].append(n)
        else:
            dict[n.ad] = [n]

def print_add(em):
    for i,n in enumerate(em):
        print(i, n.ad)

def getMinimumEmployees(e):
    em = [Node(0, None)]
    for i, com in enumerate(e):
        em.append(Node(i+1, em[com[0]], is_burnt=com[1]==0))

    dict = {}
    cnt = 0
    for i, n in enumerate(em):
        n.count()
        make_dict(dict=dict, n=n)

    keys = sorted(dict.keys(), reverse=True)
    while len(keys) > 0:
        cnt += 1
        key = keys[0]
        n = dict[key][0]

        if n.ad > 0:
            send(n)

        ndict = {}
        for i, n in enumerate(em):
            n.count()
            make_dict(dict=ndict, n=n)
        dict = ndict
        keys = sorted(dict.keys(), reverse=True)
    return cnt



def test(i, o):
    res = getMinimumEmployees(i)
    assert res == o, 'Expected %s. Got %s' % (str(o), str(res))

i = [(0, 0), (1, 0), (2, 0), (2, 0)]
test(i, 1)

i = [(0, 0), (0, 0), (1, 0)]
test(i, 2)

i = []
test(i, 0)

i = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
test(i, 1)

i = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
test(i, 2)

i = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
test(i, 2)
#
i = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (3, 0)]
test(i, 3)

i = [(0, 0), (1, 0), (2, 0), (1, 0), (2, 0)]
test(i, 2)

i = [(0, 0), (1, 0), (2, 0), (1, 0), (2, 0)]
test(i, 2)

i = [(0, 0), (0, 0), (1, 1), (3, 0), (3, 0)]
test(i, 2)

i = [(0, 1), (1, 0), (2, 1), (1, 1), (0, 1), (2, 0), (5, 1)]
test(i, 1)

i = [(0, 1), (1, 0), (2, 0), (3, 0), (1, 1), (5, 0), (5, 0), (6, 1), (8, 0)]
test(i, 3)

i = [(0, 0), (1, 0), (2, 0), (1, 0), (4, 0), (5, 0), (5, 0), (4, 0), (8, 0), (8, 0)]
test(i, 3)

i = [(0, 0), (1, 0), (1, 0), (3, 0), (4, 0), (4, 0), (3, 0), (7, 0), (7, 0)]
test(i, 3)

i = [(0, 0), (1, 1), (2, 0), (3, 0), (4, 0), (5, 0), (0, 0)]
test(i, 3)