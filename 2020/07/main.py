from collections import defaultdict

def find_children_r(d, n):
    q = 0
    ch = frozenset(c for c in d[n])
    if not ch:
        return frozenset(), 0
    else:
        for n, k in ch:
            cn, qn = find_children_r(d, n)
            ch |= cn
            q += k + k * qn
        return ch, q

def f1(c, d, t='shiny gold'):
    print('d len ' ,len(d))
    return any(e==t or f1(e, d, t) for e, _ in d[c])

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        data = f.read().strip()

        sentences = data.split('.')[:-1]
        d = defaultdict(set)
        for s in sentences:
            k = s.split('bags')[0].strip()
            v = s.split('contain')[1]
            for x in v.split(','):
                w = x.strip().split()
                q = w[0]
                if q != 'no':
                    c = x.split(q)[1].strip().split('bag')[0]
                    d[k].add((c.strip(), int(q)))
                else:
                    d[k].add(('', 0))

        print(len(d))
        f1_ = lambda x: f1(x, d, 'shiny gold')
        print(sum(map(f1_, d.copy())))

        #s = 0
        #for k in d.keys():
        #    for c, _ in find_children_r(d.copy(), k)[0]:
        #        if 'shiny gold' in c:
        #            s += 1
        #print(s)

        #print(find_children_r(d, 'shiny gold')[1])
