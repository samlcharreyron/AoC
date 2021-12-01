from collections import defaultdict
from itertools import product
import time

def get_neighbors(p, dims=3):
    pools = product((-1, 0, 1), repeat=dims)
    for prod in pools:
        if prod != tuple([0]*dims):
            yield tuple(pc + prodc for (pc, prodc) in zip(p, prod))

def p1(data):
    d = defaultdict(lambda: '.')
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            d[(i, j, 0)] = c

    for _ in range(6):
        d_ = d.copy()
        to_visit = set(d.keys())
        for k in list(d.keys()):
            to_visit |= set(n for n in get_neighbors(k))
        for k in to_visit:
            if d[k] == '#' and sum(d[n] == '#' for n in get_neighbors(k)) not in (2, 3):
                d_[k] = '.'
            if d[k] == '.' and sum(d[n] == '#' for n in get_neighbors(k)) == 3:
                d_[k] = '#'
        d = d_

    return sum(v == '#' for v in d.values())

def p2(data):
    d = defaultdict(lambda: '.')
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            d[(i, j, 0, 0)] = c

    for _ in range(6):
        #changes = []
        d_ = d.copy()
        to_visit = set(d.keys())
        for k in list(d.keys()):
            to_visit |= set(n for n in get_neighbors(k, 4))
        for k in to_visit:
            if d[k] == '#' and sum(d[n] == '#' for n in get_neighbors(k, 4)) not in (2, 3):
                #changes.append((k, '.'))
                d_[k] = '.'
            if d[k] == '.' and sum(d[n] == '#' for n in get_neighbors(k, 4)) == 3:
                #changes.append((k, '#'))
                d_[k] = '#'
        d = d_
        #for k, v in changes:
        #    d[k] = v

    return sum(v == '#' for v in d.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    print(p1(data))
    tick = time.time()
    print(p2(data))
    tock = time.time()
    print('elapsed ', tock - tick)
        
