from math import sqrt, ceil

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

    nc = 1
    while nc != 0:
        m_ = m.copy()
        nc = 0
        #import pdb; pdb.set_trace()
        for k in m.keys():
            ns = []
            for d in dr:
                for j in range(1, md):
                    if (k + j * d) in m.keys():
                        ns.append(k + j * d)
                        break

            if m[k] == 'L' and not any(m[n] == '#' for n in ns):
                m_[k] = '#'
                nc += 1
            elif m[k] == '#' and (sum(m[n] == '#' for n in ns) > 4):
                m_[k] = 'L'
                nc += 1
        m = m_

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
        print(p2(m.copy()))

