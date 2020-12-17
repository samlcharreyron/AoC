from collections import defaultdict
from itertools import product

def get_neighbors(p):
    pools = product((-1, 0, 1), repeat=3)
    for prod in pools:
        if prod != (0, 0, 0):
            yield (p[0] + prod[0], p[1] + prod[1], 
                    p[2] + prod[2])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        
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

        print(sum(v == '#' for v in d.values()))

