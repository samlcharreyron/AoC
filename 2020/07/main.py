from collections import defaultdict

def find_children(d, n):
    s = set(c for c,_ in d[n])
    children = set(c for c,_ in d[n])
    while s:
        c = s.pop()
        for k, q in d[c]:
            children.add(k)
            s.add(k)
    return children

def find_children_r(d, n, q=0):
    #import pdb; pdb.set_trace()
    ch = frozenset(c for c in d[n])
    if not ch:
        return frozenset(), 0
    else:
        for n, k in ch:
            cn, qn = find_children_r(d, n)
            ch |= cn
            q += k + k * qn
        return ch, q

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
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
        #print(d)
        #print(find_children_r(d, 'light red'))
        #print(sum(('shiny gold' in find_children_r(d.copy(), k)[0] for k in d.keys())))
        print(find_children_r(d.copy(), 'shiny gold'))
        #print(find_children_r(d.copy(), 'faded blue'))
        #print(find_children_r(d.copy(), 'dark olive'))
