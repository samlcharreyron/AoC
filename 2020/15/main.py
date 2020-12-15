import time
from dataclasses import dataclass

@dataclass
class Number:
    i: int
    j: int

def p(data, l):
    d = dict()
    i = 1
    for n in data:
        d[n] = Number(i, 0)
        i += 1

    tick = time.time()
    for i in range(len(data) + 1, l):
        if d[n].j == 0:
            n = 0
        else:
            n = d[n].i - d[n].j

        if n not in d:
            d[n] = Number(i, 0)
        else:
            d[n].j = d[n].i
            d[n].i = i
            #d[n].n += 1 
    
    return n

def p_(data, l):
    d = dict()
    i = 1
    for n in data:
        d[n] = (i, 0)
        i += 1

    tick = time.time()
    for i in range(len(data) + 1, l):
        dni, dnj = d[n]
        if dni == 0:
            n = 0
        else:
            n = dni - dnj

        if n not in d:
            d[n] = (i, 0)
        else:
            d[n] = (i, dni)
    
    return n

if __name__ == '__main__':
    #data = [0, 3, 6]
    data = [0,1,4,13,15,12,16]
    tick = time.time()
    n = p(data, 2021)
    tock = time.time()
    print(n, ' in ', tock - tick, ' s' )

    tick = time.time()
    n = p_(data, 30000001)
    tock = time.time()
    print(n, ' in ', tock - tick, ' s' )
