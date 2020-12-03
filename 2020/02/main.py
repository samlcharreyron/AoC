def p1(lines):
    v = []
    for line in lines:
        l, h = line.split()[0].split('-')
        l = int(l)
        h = int(h)
        c = line.split()[1][0]
        p = line.split()[2]
        n = p.count(c)
        if n >= l and n <= h:
            v.append(p)

    print(len(v))

def p2(lines):
    v= []
    for line in lines:
        l, h = line.split()[0].split('-')
        l = int(l)
        h = int(h)
        c = line.split()[1][0]
        p = line.split()[2]
        if (p[l-1] == c) != (p[h-1] == c):
            v.append(p)
    print(len(v))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    p1(lines)
    p2(lines)

