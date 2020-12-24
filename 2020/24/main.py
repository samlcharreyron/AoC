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

if __name__ == '__main__':
    grid = defaultdict(bool)
    flipped = defaultdict(int)

    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        
        for line in lines:
            p = (0, 0, 0)
            for m in gen_dirs(line):
                p = tuple(a + b for a, b in zip(p, dirs[m]))

            grid[p] = not grid[p]
            flipped[p] += 1

        #print(grid)
        #print(sum(v == 1 for v in flipped.values()))
        #print(sum(v == 2 for v in flipped.values()))
        #print(sum(v == 3 for v in flipped.values()))
        print(sum(grid.values()))


