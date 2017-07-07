import difflib
import heapq



def parse_name(filename):
    number = 0
    if filename[-1] == ')':
        index = len(filename) - 2
        base = 1
        while filename[index] != '(':
            number = number + int(filename[index]) * base
            index -= 1
            base *= 10
        filename = filename[:index]
    return filename, number


def create(filename, files):
    if filename in files:
        fset, fheap = files[filename]
        cnt = heapq.heappop(fheap)
        if len(fheap) == 0:
            fheap.append(cnt + 1)

        fset.add(cnt)

        if cnt != 0:
            filename = '%s(%d)' % (filename, cnt)
    else:
        heap = [1]
        files[filename] = [set([0]), heap]
    return filename


def delete(filename, files):
    filename, number = parse_name(filename)
    fset, fheap = files[filename]
    fset.remove(number)
    heapq.heappush(fheap, number)


def execute(command, files):
    opts = command.split(' ')
    op = opts[0]
    if op == 'crt':
        filename = opts[1]
        filename = create(filename, files)
        print('+', filename)
    elif op == 'del':
        filename = opts[1]
        delete(filename, files)
        print('-', filename)
    elif op == 'rnm':
        filename = opts[1]
        new_filename = opts[2]

        delete(filename, files)
        new_filename = create(new_filename, files)
        print('r %s -> %s' % (filename, new_filename))
    else:
        pass
