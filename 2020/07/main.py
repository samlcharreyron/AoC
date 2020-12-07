from collections import defaultdict

def find_children(d, n):
    s = set(c for c,_ in d[n])
    v = set()
    children = set(c for c,_ in d[n])
    while s:
        c = s.pop()
        v.add(c)
        for k, q in d[c]:
            children.add(k)
            if k not in v:
                s.add(k)
    return children

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
                    d[k].add((c.strip(), q))
        print(sum(('shiny gold' in find_children(d.copy(), k) for k in d.keys())))
