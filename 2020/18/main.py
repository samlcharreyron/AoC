import operator
from functools import reduce
import time

def f_(sub):
    r = int(sub[-1])
    o = sub[-2]

    if len(sub) == 3:
        if o == '+':
            return r + int(sub[0])
        else:
            return r * int(sub[0])
    else:
        if o == '+':
            return r + f(sub[:-2])
        else:
            return r * f(sub[:-2])
def f(sub):
    ops = {'+': operator.add, '*': operator.mul}
    ol = sub[1::2]
    al = (int(a) for a in sub[0::2])
    it = iter(al)
    val = next(it)

    for o, a in zip(ol, it):
        val = ops[o](val, a)
    return val

def f2(line):
    ac = []
    for sub in line.split('*'):
        ac.append(sum(int(a) for a in sub.split('+')))
    return reduce(operator.mul, ac)

def evalu(line, p1=True):
    while '(' in line:
        s = []
        subs = []
        t = 0
        for i, c in enumerate(line):
            if c == '(':
                s.append(i)
            elif c == ')':
                b = s.pop()
                subs.append((b, i))

        line_ = line
        for s, e in subs:
            sub = line[s+1:e]
            if '(' not in sub:
                if p1:
                    line_ = line_.replace(line[s:e+1], '{}'.format(f(sub.split())))
                else:
                    line_ = line_.replace(line[s:e+1], '{}'.format(f2(sub)))
        line = line_
    if p1:
        return f(line.split())
    else:
        return f2(line)

if __name__ == '__main__':
    with open('input.txt', 'r') as fe:
        data = fe.read().splitlines()
    tick = time.time()
    print(sum(evalu(line, p1=True) for line in data))
    tock = time.time()
    print('elapsed ', tock - tick)

    print(sum(evalu(line, p1=False) for line in data))
