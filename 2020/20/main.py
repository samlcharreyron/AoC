import numpy as np
from dataclasses import dataclass
from collections import defaultdict
from functools import reduce
import operator

moves = {
        ('l', 'l', True) : [['R180', 'FTB'], ['FLR']],
        ('l', 'r', True) : [[]],
        ('r', 'l', True) : [[]],
        ('l', 't', True) : [['R90']],
        ('t', 'l', True) : [['R-90']],
        ('l', 'b', True) : [['R90', 'FLR'], ['R-90', 'FTB']],
        ('b', 'l', True) : [['R-90', 'FLR'], ['R90', 'FTB']],
        ('r', 'r', True) : [['FLR'], ['R180', 'FTB']],
        ('r', 't', True) : [['R-90', 'FTB'], ['R90', 'FLR']],
        ('t', 'r', True) : [['R90', 'FTB'], ['-R90', 'FLR']],
        ('r', 'b', True) : [['R-90']],
        ('b', 'r', True) : [['R90']],
        ('t', 'b', True) : [[]],
        ('b', 't', True) : [[]],
        ('t', 't', True) : [['R180', 'FLR'], ['FTB']],
        ('b', 'b', True) : [['R180', 'FLR'], ['FTB']],
        ('l', 'l', False) : [['R180'], ['FLR', 'FTB']],
        ('l', 'r', False) : [['R180', 'FLR'], ['FTB']],
        ('r', 'l', False) : [['R180', 'FLR'], ['FTB']],
        ('l', 't', False) : [['R-90', 'FLR'], ['R90', 'FTB']],
        ('t', 'l', False) : [['R90', 'FLR'], ['R-90', 'FTB']],
        ('l', 'b', False) : [['R-90']],
        ('b', 'l', False) : [['R90']],
        ('r', 'r', False) : [['R180'], ['FLR', 'FTB']],
        ('r', 't', False) : [['R90']],
        ('t', 'r', False) : [['-R90']],
        ('r', 'b', False) : [['R90', 'FTB'], ['R-90', 'FLR']],
        ('b', 'r', False) : [['R-90', 'FTB'], ['R90', 'FLR']],
        ('t', 'b', False) : [['FLR'], ['R180', 'FTB']],
        ('b', 't', False) : [['FLR'], ['R180', 'FTB']],
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
            d[tna].append(('l', 'l', False, tnb))
            d[tnb].append(('l', 'l', False, tna))
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('l', 'r', False, tnb))
            d[tnb].append(('r', 'l', False, tna))
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('l', 't', False, tnb))
            d[tnb].append(('t', 'l', False, tna))
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('l', 'b', False, tnb))
            d[tnb].append(('b', 'l', False, tna))
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].append(('l', 'l', True, tnb))
            d[tnb].append(('l', 'l', True, tna))
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('l', 'r', True, tnb))
            d[tnb].append(('r', 'l', True, tna))
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('l', 't', True, tnb))
            d[tnb].append(('t', 'l', True, tna))
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('l', 'b', True, tnb))
            d[tnb].append(('b', 'l', True, tna))

    while rbs:
        b = rbs.pop()
        tna = tnrs.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].append(('r', 'l', False, tnb))
            d[tnb].append(('l', 'r', False, tna))
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('r', 'r', False, tnb))
            d[tnb].append(('r', 'r', False, tna))
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('r', 't', False, tnb))
            d[tnb].append(('t', 'r', False, tna))
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('r', 'b', False, tnb))
            d[tnb].append(('b', 'r', False, tna))
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].append(('r', 'l', True, tnb))
            d[tnb].append(('l', 'r', True, tna))
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('r', 'r', True, tnb))
            d[tnb].append(('r', 'r', True, tna))
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('r', 't', True, tnb))
            d[tnb].append(('t', 'r', True, tna))
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('r', 'b', True, tnb))
            d[tnb].append(('b', 'r', True, tna))

    while tbs:
        b = tbs.pop()
        tna = tnts.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].append(('t', 'l', False, tnb))
            d[tnb].append(('l', 't', False, tna))
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('t', 'r', False, tnb))
            d[tnb].append(('r', 't', False, tna))
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('t', 't', False, tnb))
            d[tnb].append(('t', 't', False, tna))
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('t', 'b', False, tnb))
            d[tnb].append(('b', 't', False, tna))
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].append(('t', 'l', True, tnb))
            d[tnb].append(('l', 't', True, tna))
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('t', 'r', True, tnb))
            d[tnb].append(('r', 't', True, tna))
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('t', 't', True, tnb))
            d[tnb].append(('t', 't', True, tna))
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('t', 'b', True, tnb))
            d[tnb].append(('b', 't', True, tna))

    while bbs:
        b = bbs.pop()
        tna = tnbs.pop()
        if b in lbs:
            idx = lbs.index(b)
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].append(('b', 'l', False, tnb))
            d[tnb].append(('l', 'b', False, tna))
        elif b in rbs:
            idx = rbs.index(b)
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('b', 'r', False, tnb))
            d[tnb].append(('r', 'b', False, tna))
        elif b in tbs:
            idx = tbs.index(b)
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('b', 't', False, tnb))
            d[tnb].append(('t', 'b', False, tna))
        elif b in bbs:
            idx = bbs.index(b)
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('b', 'b', False, tnb))
            d[tnb].append(('b', 'b', False, tna))
        elif b[::-1] in lbs:
            idx = lbs.index(b[::-1])
            lbs.pop(idx)
            tnb = tnls.pop(idx)
            d[tna].append(('b', 'l', True, tnb))
            d[tnb].append(('l', 'b', True, tna))
        elif b[::-1] in rbs:
            idx = rbs.index(b[::-1])
            rbs.pop(idx)
            tnb = tnrs.pop(idx)
            d[tna].append(('b', 'r', True, tnb))
            d[tnb].append(('r', 'b', True, tna))
        elif b[::-1] in tbs:
            idx = tbs.index(b[::-1])
            tbs.pop(idx)
            tnb = tnts.pop(idx)
            d[tna].append(('b', 't', True, tnb))
            d[tnb].append(('t', 'b', True, tna))
        elif b[::-1] in bbs:
            idx = bbs.index(b[::-1])
            bbs.pop(idx)
            tnb = tnbs.pop(idx)
            d[tna].append(('b', 'b', True, tnb))
            d[tnb].append(('b', 'b', True, tna))

    corners = [k for k, t in d.items() if len(t) < 3]
    
    print(corners)
    print(reduce(operator.mul, corners))

    to_visit = set(corners)

    while to_visit:
        t = to_visit.pop()
        for edge in d[t]:
            for move in moves[edge[0:3]]:
                print(move)


        #if d[t].lb == (-1, 'n') and d[t].tb == (-1, 'n ):
        #    print('top left ', t)
