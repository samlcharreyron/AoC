import re
from sys import exit

mem = dict()

def p1(data):
    for p in data.split('mask = ')[1:]:
        mk = p.splitlines()[0] 
        for l in p.splitlines()[1:]:
            a, v = (int(d) for d in re.search(r'mem\[(\d+)\] = (\d+)', l).groups())
            vb = list('{:036b}'.format(v))
            for i, mc in enumerate(mk):
                if mc != 'X':
                    vb[i] = mc
            mem[a] = int(''.join(vb),2)
    return(sum(v for v in mem.values()))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().strip()
        print(p1(data))
