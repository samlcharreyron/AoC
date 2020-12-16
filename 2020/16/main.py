import re
from collections import namedtuple
from functools import reduce
import operator

Field = namedtuple('Field', ['f', 'l1', 'u1', 'l2', 'u2'])

def p1(data):
    conds, tkt, ntix = data.split('\n\n')

    fields = []
    for cond in conds.splitlines():
        m = re.match(r'((\w+\s)*\w+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)', cond)
        f, _, l1, u1, l2, u2 = m.groups()
        fields.append(Field(f, int(l1), int(u1), int(l2), int(u2)))

    mt = [int(i) for i in tkt.splitlines()[1].split(',')]
    nts = [[int(i) for i in l.split(',')] for l in ntix.splitlines()[1:]]

    check = lambda f, tv: ( f.l1 <= tv <= f.u1) or ( f.l2 <= tv <= f.u2)

    return sum(tv for t in nts for tv in t if all(not check(f, tv) for f in fields))

def p2(data):
    conds, tkt, ntix = data.split('\n\n')

    fields = []
    for cond in conds.splitlines():
        m = re.match(r'((\w+\s)*\w+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)', cond)
        f, _, l1, u1, l2, u2 = m.groups()
        fields.append(Field(f, int(l1), int(u1), int(l2), int(u2)))

    mt = [int(i) for i in tkt.splitlines()[1].split(',')]
    nts = [[int(i) for i in l.split(',')] for l in ntix.splitlines()[1:]]

    check = lambda f, tv: ( f.l1 <= tv <= f.u1) or ( f.l2 <= tv <= f.u2)

    invalid = set(i for i, t in enumerate(nts) for tv in t for f in fields if all(not check(f, tv) for f in fields))
    valid = [t for i, t in enumerate(nts) if i not in invalid]
    valid.append(mt)
    validt = [[c for c in r] for r in valid]

    N = len(fields)
    field_names = set(f.f for f in fields)
    can_be = [field_names.copy() for _ in range(N)]
    for t in valid:
        for i, tv in enumerate(t):
            can_be[i] -= set(f.f for f in fields if not check(f, tv))
    
    while any(len(can_be[i]) > 1 for i in range(N)):
        remove = dict()
        for i in range(N):
            if len(can_be[i]) == 1:
                remove[i] = can_be[i]

        for k, v in remove.items():
            for i in range(N):
                if i != k:
                    can_be[i] -= v
    vals = [v for f,v in zip(can_be, mt) if 'departure' in f.pop()]
    return reduce(operator.mul, vals, 1)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
        print(p1(data))
        print(p2(data))
