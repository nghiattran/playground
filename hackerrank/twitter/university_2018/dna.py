def distance(a, b):
    cnt = 0
    for i in range(8):
        cnt += 0 if a[i] == b[i] else 1
    return cnt

def findMutationDistance(start, end, bank):
    stack = [(start, 0)]
    cnt = 0
    while len(stack) > 0:
        current, level = stack.pop()
        cnt += 1
        i = 0
        while i < len(bank):
            dna = bank[i]
            dst = distance(current, dna)

            if dst == 1:
                if dna == end:
                    return level + 1

                bank.remove(dna)
                stack.append((dna, level + 1))
            else:
                i += 1
        print(cnt)
    return -1

def gen(prefix, res):
    if len(prefix) == 8:
        res.append(prefix)
        return

    for c in ['A', 'G', 'T', 'C']:
        gen(prefix + c, res)

inp = """AAAAAAAA
AAAAAATT
4
AAAAAAAA
AAAAAAAT
AAAAAATT
AAAAGATT
AAAAAATT
AAAAAATT
ATTAAATT
AGAATATT
ATAAAATT
AAAAATTT"""

entries = inp.split('\n')
start = entries[0]
end = entries[1]
bank = entries[3:]

print(findMutationDistance(start, end, bank))


inp = """AAAAAAAA
GGAAAAAA
4
GAAAAAAA
AAGAAAAA
AAAAGAAA
GGAAAAAA"""

entries = inp.split('\n')
start = entries[0]
end = entries[1]
bank = entries[3:]

print(findMutationDistance(start, end, bank))

start = 'A' * 8
end = 'T' * 8
bank = []
gen('', bank)

print(findMutationDistance(start, end, bank))
