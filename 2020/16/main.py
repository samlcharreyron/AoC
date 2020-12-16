import re
from dataclasses import dataclass
from collections import namedtuple

Field = namedtuple('Field', ['f', 'l1', 'u1', 'l2', 'u2'])

#@dataclass
#class Field:
#    f: str
#    l1: int
#    u1: int
#    l2: int
#    u2: int

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

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()
        print(p1(data))


