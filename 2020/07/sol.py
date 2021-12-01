from parse import *

x = {search('{} bag', x)[0]: [findall('{:d} {} bag', x)]
        for x in open('input.txt')}
t = 'shiny gold'

def f(c): return any(d==t or f(d) for _,d in x[c])
def g(c): return sum(n + n * g(d) for n,d in x[c])

print(g(t))
#print(sum(map(f, x)), g(t))
