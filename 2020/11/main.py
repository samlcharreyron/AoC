from math import sqrt, ceil
from collections import defaultdict
import time

def p1(m):
    adj = (complex(-1,0), complex(1, 0), complex(0, -1), complex(0, 1),
            complex(-1, -1), complex(-1,1), complex(1, -1), complex(1,1))

    nc = 1
    while nc != 0:
        m_ = m.copy()
        nc = 0
        for k, v in m_.items():
            ns = [m[k+a] for a in adj if (k+a) in m.keys()]
            if m[k] == 'L' and not any(n == '#' for n in ns):
                m_[k] = '#'
                nc += 1
            elif m[k] == '#' and sum(n == '#' for n in ns) > 3:
                m_[k] = 'L'
                nc += 1
        m = m_

    return sum(v == '#' for v in m.values())

def p2(m):
    dr = (complex(-1,0), complex(1, 0), complex(0, -1), complex(0, 1),
            complex(-1, -1), complex(-1,1), complex(1, -1), complex(1,1))

    md = 2 * ceil(sqrt(pow(max(k.real for k in m.keys()), 2) + pow(max(k.imag for k in m.keys()), 2)))

    # find neighbors
    nb = defaultdict(list)
    for k in m.keys():
        for d in dr:
            for j in range(1, md):
                if (k + j * d) in m.keys():
                    nb[k].append(k+j*d)
                    break

    changed = set(m.keys())
    changes = ['d']
    while changes:
        changes = []

        for k in m.keys() & changed:
            if m[k] == 'L' and not any(m[n] == '#' for n in nb[k]):
                changes.append((k, '#'))
            elif m[k] == '#' and (sum(m[n] == '#' for n in nb[k]) > 4):
                changes.append((k, 'L'))

        for k, v in changes:
            m[k] = v

        changed = set(k for k,_ in changes)

    return sum(v == '#' for v in m.values())

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        m = dict()
        for i, line in enumerate(data):
            for j, c in enumerate(line):
                if c in ['#', 'L']:
                    m[complex(j, i)] = c

        #print(p1(m.copy()))
        tick = time.time()
        print(p2(m.copy()))
        tock = time.time()
        print('elapsed: ', tock - tick, ' s')

