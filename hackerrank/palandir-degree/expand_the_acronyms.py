dictionary = {}


def parse_abbr(entry, i):
    i += 1
    abbr = ''
    while entry[i] != ')':
        abbr += entry[i]
        i += 1
    return abbr, i


def parse_real(entry, abbr, i):
    i -= 2
    end_pos = i
    stop = False
    name = ''
    uppercase_cnt = 0
    while not stop and i >= 0:
        name = entry[i] + name
        uppercase_cnt += 1 if 'A' <= entry[i] and entry[i] <= 'Z' else 0
        stop = uppercase_cnt == len(abbr)
        i -= 1
    return name


def parse(entry):
    i = 0
    while i < len(entry):
        ch = entry[i]
        if ch == '(':
            start_abbr = i
            abbr, i = parse_abbr(entry, i)
            name = parse_real(entry, abbr, start_abbr)
            dictionary[abbr] = name
        i += 1


snippets = """The United Nations Children's Fund (UNICEF) is a United Nations Programme headquartered in New York City, that provides long-term humanitarian and developmental assistance to children and mothers in developing countries.
The National University of Singapore is a leading global university located in Singapore, Southeast Asia. NUS is Singapore's flagship university which offers a global approach to education and research.
Massachusetts Institute of Technology (MIT) is a private research university located in Cambridge, Massachusetts, United States."""

snippets = snippets.split('\n')
for s in snippets:
    parse(s)

print(dictionary)