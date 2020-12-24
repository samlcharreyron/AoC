import numpy as np
from collections import defaultdict

dirs = {
        'e': (-1, 0, 1),
        'se': (-1, 1, 0),
        'sw': (0, 1, -1),
        'w': (1, 0, -1),
        'nw': (1, -1, 0),
        'ne': (0, -1, 1)
        }

def gen_dirs(line):
    i = 0
    while i < len(line):
        if i == len(line) - 1:
            yield line[i]
            i+= 1
        else:
            c1, c2 = line[i:i+2]
            if (c1 + c2) in dirs:
                i += 2
                yield c1 + c2
            else:
                i+= 1
                yield c1

def p1(lines):
    grid = defaultdict(bool)

    for line in lines:
        p = (0, 0, 0)
        for m in gen_dirs(line):
            p = tuple(a + b for a, b in zip(p, dirs[m]))

        grid[p] = not grid[p]

    return sum(grid.values())

def p2(lines):
    grid = defaultdict(bool)

    for line in lines:
        p = (0, 0, 0)
        for m in gen_dirs(line):
            p = tuple(a + b for a, b in zip(p, dirs[m]))

        grid[p] = not grid[p]

    for i in range(1, 101):
        to_flip = set()
        to_visit = set(grid.keys())
        for p in to_visit.copy():
            nbrs = set(tuple(a+b for a, b in zip(p, dp)) for dp in dirs.values())
            to_visit |= nbrs

        for p in to_visit:
            nbrs = [tuple(a+b for a, b in zip(p, dp)) for dp in dirs.values()]
            if grid[p]:
                num_b = sum(grid[nb] for nb in nbrs)
                if num_b == 0 or num_b > 2:
                    to_flip.add(p)
            else:
                num_b = sum(grid[nb] for nb in nbrs)
                if num_b == 2:
                    to_flip.add(p)

        for p in to_flip:
            grid[p] = not grid[p]

        print('Day ', i, sum(v for v in grid.values()))

    return(sum(v for v in grid.values()))
            

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    print(p1(lines))
    print(p2(lines))

