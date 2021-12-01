import re
from sys import exit
from collections import OrderedDict, namedtuple
from itertools import product

class Entry:
    def __init__(self, v, n):
        self.v = v
        self.n = n

    def __repr__(self):
        return 'n: {}, v: {}'.format(self.n, self.v)

def p1(data):
    mem = dict()
    for p in data.split('mask = ')[1:]:
        mk = p.splitlines()[0] 
        for l in p.splitlines()[1:]:
            a, v = (int(d) for d in re.search(r'mem\[(\d+)\] = (\d+)', l).groups())
            vb = list('{num:0{width}b}'.format(width=len(mk),num=v))
            for i, mc in enumerate(mk):
                if mc != 'X':
                    vb[i] = mc
            mem[a] = int(''.join(vb),2)
    return(sum(v for v in mem.values()))

def overlap(ab1, ab2):
    n0 = sum(c1!= 'X' and c2 != 'X' and c1 != c2 for c1, c2 in zip(ab1, ab2))
    n1 = sum((c1 == 'X' and c2 != 'X') or (c1 != 'X' and c2 == 'X') for c1, c2 in zip(ab1, ab2))
    n2 = sum((c1 == 'X' and c2 == 'X') for c1, c2 in zip(ab1, ab2))
    if n0:
        return 0
    else:
        return pow(2, n2)

def address(a, mk):
    ab = list('{num:0{width}b}'.format(width=len(mk),num=a))
    for i, c in enumerate(mk):
        if c != '0':
            ab[i] = c
    return ''.join(ab)

def p2(data):
    mem = dict()
    abl = []
    for p in data.split('mask = ')[1:]:
        mk = list(p.splitlines()[0])
        for l in p.splitlines()[1:]:
            a, v = (int(d) for d in re.search(r'mem\[(\d+)\] = (\d+)', l).groups())
            ab = address(a, mk)
            mem[ab] = Entry(v=v, n=0)

    abl = list(mem.keys())
    assert(abl[-1] == address(47560, list('11X010X0X0100X011X11XX01110000001101')))
    assert(abl[0]  == address(30904, list('11X01X101X10000110110101X100000011XX')))

    for i, ab1 in enumerate(abl):
        ne = pow(2, sum(c == 'X' for c in ab1))
        no = sum(overlap(ab1, abl[j]) for j in range(i+1, len(abl)))
        print('{}: entries: {}, overlap: {}'.format(i, ne, no))
        mem[ab1].n = ne - no

    return sum(e.v * e.n for e in mem.values())

def get_addresses(ab):
    idxs = [i for i, c in enumerate(ab) if c == 'X']
    nx = len(idxs)
    ad_l = []
    abl = list(ab)
    for c in product('01', repeat=nx):
        for ix, b in zip(idxs, c):
            abl[ix] = b
        ad_l.append(''.join(abl))
    return ad_l

def p2_(data):
    mem = dict()
    for p in data.split('mask = ')[1:]:
        mk = list(p.splitlines()[0])
        for l in p.splitlines()[1:]:
            a, v = (int(d) for d in re.search(r'mem\[(\d+)\] = (\d+)', l).groups())
            ab = list(address(a, mk))
            idxs = [i for i, c in enumerate(ab) if c == 'X']
            nx = len(idxs)
            for c in product('01', repeat=nx):
                for ix, b in zip(idxs, c):
                    ab[ix] = b
                mem[int(''.join(ab), 2)] = v
    return sum(v for v in mem.values())


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().strip()
        print(p1(data))
        print(p2(data))
