import numpy as np
from dataclasses import dataclass
from collections import defaultdict
from functools import reduce
import operator

moves = {
        ('l', 'l', True) : [['R180', 'FTB'], ['FLR']],
        ('l', 'r', True) : [[]],
        ('l', 't', True) : [['R90']],
        ('l', 'b', True) : [['R90', 'FLR'], ['R-90', 'FTB']],
        ('r', 'r', True) : [['FLR'], ['R180', 'FTB']],
        ('r', 't', True) : [['R-90', 'FTB'], ['R90', 'FLR']],
        ('r', 'b', True) : [['R-90']],
        ('t', 'b', True) : [[]],
        ('t', 't', True) : [['R180', 'FLR'], ['FTB']],
        ('b', 'b', True) : [['R180', 'FLR'], ['FTB']],
        ('l', 'l', False) : [['R180'], ['FLR', 'FTB']],
        ('l', 'r', False) : [['R180', 'FLR'], ['FTB']],
        ('l', 't', False) : [['R-90', 'FLR'], ['R90', 'FTB']],
        ('l', 'b', False) : [['R-90']],
        ('r', 'r', False) : [['R180'], ['FLR', 'FTB']],
        ('r', 't', False) : [['R90']],
        ('r', 'b', False) : [['R90', 'FTB'], ['R-90', 'FLR']],
        ('t', 'b', False) : [['FLR'], ['R180', 'FTB']],
        ('t', 't', False) : [['R180'], ['FLR', 'FTB']],
        ('b', 'b', False) : [['R180'], ['FLR', 'FTB']] }

@dataclass
class Tile:
    lb: tuple
    rb: tuple
    tb: tuple
    bb: tuple

    def __init__(self):
        self.lb = (-1, 'n', False)
        self.rb = (-1, 'n', False)
        self.tb = (-1, 'n', False)
        self.bb = (-1, 'n', False)

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
    #d = defaultdict(Tile)
    d = defaultdict(list)

    with open('test.txt', 'r') as f:
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
            d[tna].lb = (tnb, 'l', False)
            d[tnb].lb = (tna, 'l', False)
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].lb = (tnb, 'r', False)
            d[tnb].rb = (tna, 'l', False)
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].lb = (tnb, 't', False)
            d[tnb].tb = (tna, 'l', False)
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].lb = (tnb, 'b', False)
            d[tnb].bb = (tna, 'l', False)
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].lb = (tnb, 'l', True)
            d[tnb].lb = (tna, 'l', True)
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].lb = (tnb, 'r', True)
            d[tnb].rb = (tna, 'l', True)
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].lb = (tnb, 't', True)
            d[tnb].tb = (tna, 'l', True)
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].lb = (tnb, 'b', True)
            d[tnb].bb = (tna, 'l', True)
        else:
            d[tna].lb = (-1, 'n', False)

    while rbs:
        b = rbs.pop()
        tna = tnrs.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].rb = (tnb, 'l', False)
            d[tnb].lb = (tna, 'r', False)
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].rb = (tnb, 'r', False)
            d[tnb].rb = (tna, 'r', False)
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].rb = (tnb, 't', False)
            d[tnb].tb = (tna, 'r', False)
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].rb = (tnb, 'b', False)
            d[tnb].bb = (tna, 'r', False)
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].rb = (tnb, 'l', True)
            d[tnb].lb = (tna, 'r', True)
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].rb = (tnb, 'r', True)
            d[tnb].rb = (tna, 'r', True)
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].rb = (tnb, 't', True)
            d[tnb].tb = (tna, 'r', True)
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].rb = (tnb, 'b', True)
            d[tnb].bb = (tna, 'r', True)
        else:
            d[tna].rb = (-1, 'n', False)

    while tbs:
        b = tbs.pop()
        tna = tnts.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].tb = (tnb, 'l', False)
            d[tnb].lb = (tna, 't', False)
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].tb = (tnb, 'r', False)
            d[tnb].rb = (tna, 't', False)
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].tb = (tnb, 't', False)
            d[tnb].tb = (tna, 't', False)
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].tb = (tnb, 'b', False)
            d[tnb].bb = (tna, 't', False)
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].tb = (tnb, 'l', True)
            d[tnb].lb = (tna, 't', True)
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].tb = (tnb, 'r', True)
            d[tnb].rb = (tna, 't', True)
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].tb = (tnb, 't', True)
            d[tnb].tb = (tna, 't', True)
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].tb = (tnb, 'b', True)
            d[tnb].bb = (tna, 't', True)
        else:
            d[tna].tb = (-1, 'n', False)

    while bbs:
        b = bbs.pop()
        tna = tnbs.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].bb = (tnb, 'l', False)
            d[tnb].lb = (tna, 'b', False)
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].bb = (tnb, 'r', False)
            d[tnb].rb = (tna, 'b', False)
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].bb = (tnb, 't', False)
            d[tnb].tb = (tna, 'b', False)
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].bb = (tnb, 'b', False)
            d[tnb].bb = (tna, 'b', False)
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].bb = (tnb, 'l', True)
            d[tnb].lb = (tna, 'b', True)
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].bb = (tnb, 'r', True)
            d[tnb].rb = (tna, 'b', True)
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].bb = (tnb, 't', True)
            d[tnb].tb = (tna, 'b', True)
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].bb = (tnb, 'b', True)
            d[tnb].bb = (tna, 'b', True)
        else:
            d[tna].bb = (-1, 'n', False)

    num_outer = lambda t: sum( x == (-1, 'n', False) for x in [t.lb, t.rb, t.tb, t.bb])
    corners = [k for k, t in d.items() if num_outer(t) > 1]
    
    print(corners)
    print(reduce(operator.mul, corners))

    to_visit = set(corners)

    while to_visit:
        t = to_visit.pop()

    for t in d:
        print(t, d[t])
        #if d[t].lb == (-1, 'n') and d[t].tb == (-1, 'n ):
        #    print('top left ', t)
