import numpy as np
from dataclasses import dataclass
from collections import defaultdict
from functools import reduce
import operator

#Tile = NamedTupe('Tile', ['lb', 'rb', 'tb', 'bb'])

@dataclass
class Tile:
    lb: tuple
    rb: tuple
    tb: tuple
    bb: tuple

    def __init__(self):
        self.n = (-1, 'n')
        self.lb = (-1, 'n')
        self.rb = (-1, 'n')
        self.tb = (-1, 'n')
        self.bb = (-1, 'n')

if __name__ == '__main__':
    #d = dict()
    lbs = []
    rbs = []
    tbs = []
    bbs = []
    tnls = []
    tnrs = []
    tnts = []
    tnbs = []
    d = defaultdict(Tile)

    with open('input.txt', 'r') as f:
       data = f.read().split('\n\n') 

       for t in data:
           tn = int(t.splitlines()[0].split()[1][:-1])
           tilet = [[c for c in line] for line in t.splitlines()[1:]]
           tile = np.array(tilet)
           #d[tn] = tile
           lbs.append(''.join(tile[:,0]))
           rbs.append(''.join(tile[:,-1]))
           tbs.append(''.join(tile[0,:]))
           bbs.append(''.join(tile[-1,:]))
           tnls.append(tn)
           tnrs.append(tn)
           tnts.append(tn)
           tnbs.append(tn)

    while lbs:
        b = lbs.pop()
        tna = tnls.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].lb = (tnb, 'l')
            d[tnb].lb = (tna, 'l')
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].lb = (tnb, 'r')
            d[tnb].rb = (tna, 'l')
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].lb = (tnb, 't')
            d[tnb].tb = (tna, 'l')
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].lb = (tnb, 'b')
            d[tnb].bb = (tna, 'l')
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].lb = (tnb, 'l')
            d[tnb].lb = (tna, 'l')
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].lb = (tnb, 'r')
            d[tnb].rb = (tna, 'l')
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].lb = (tnb, 't')
            d[tnb].tb = (tna, 'l')
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].lb = (tnb, 'b')
            d[tnb].bb = (tna, 'l')
        else:
            d[tna].lb = (-1, 'n')

    while rbs:
        b = rbs.pop()
        tna = tnrs.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].rb = (tnb, 'l')
            d[tnb].lb = (tna, 'r')
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].rb = (tnb, 'r')
            d[tnb].rb = (tna, 'r')
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].rb = (tnb, 't')
            d[tnb].tb = (tna, 'r')
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].rb = (tnb, 'b')
            d[tnb].bb = (tna, 'r')
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].rb = (tnb, 'l')
            d[tnb].lb = (tna, 'r')
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].rb = (tnb, 'r')
            d[tnb].rb = (tna, 'r')
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].rb = (tnb, 't')
            d[tnb].tb = (tna, 'r')
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].rb = (tnb, 'b')
            d[tnb].bb = (tna, 'r')
        else:
            d[tna].rb = (-1, 'n')

    while tbs:
        b = tbs.pop()
        tna = tnts.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].tb = (tnb, 'l')
            d[tnb].lb = (tna, 't')
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].tb = (tnb, 'r')
            d[tnb].rb = (tna, 't')
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].tb = (tnb, 't')
            d[tnb].tb = (tna, 't')
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].tb = (tnb, 'b')
            d[tnb].bb = (tna, 't')
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].tb = (tnb, 'l')
            d[tnb].lb = (tna, 't')
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].tb = (tnb, 'r')
            d[tnb].rb = (tna, 't')
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].tb = (tnb, 't')
            d[tnb].tb = (tna, 't')
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].tb = (tnb, 'b')
            d[tnb].bb = (tna, 't')
        else:
            d[tna].tb = (-1, 'n')

    while bbs:
        b = bbs.pop()
        tna = tnbs.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].bb = (tnb, 'l')
            d[tnb].lb = (tna, 'b')
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].bb = (tnb, 'r')
            d[tnb].rb = (tna, 'b')
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].bb = (tnb, 't')
            d[tnb].tb = (tna, 'b')
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].bb = (tnb, 'b')
            d[tnb].bb = (tna, 'b')
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].bb = (tnb, 'l')
            d[tnb].lb = (tna, 'b')
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].bb = (tnb, 'r')
            d[tnb].rb = (tna, 'b')
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].bb = (tnb, 't')
            d[tnb].tb = (tna, 'b')
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].bb = (tnb, 'b')
            d[tnb].bb = (tna, 'b')
        else:
            d[tna].bb = (-1, 'n')
    
    num_outer = lambda t: sum( x == (-1, 'n') for x in [t.lb, t.rb, t.tb, t.bb])
    corners = [k for k, t in d.items() if num_outer(t) > 1]

    assert(len(corners) == 4)
    
    print(corners)
    print(reduce(operator.mul, corners))
