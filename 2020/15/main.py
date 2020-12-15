import time

class Number:
    def __init__(self, i, j, n):
        self.i = i
        self.n = n
        self.j = j

    def __repr__(self):
        return 'i: {}, j: {}, n: {}'.format(self.i, self.j, self.n)

def p(data, l):
    d = dict()
    i = 1
    for n in data:
        d[n] = Number(i, 0, 1)
        i += 1

    tick = time.time()
    for i in range(len(data) + 1, l):
        if d[n].n == 1:
            n = 0
        else:
            n = d[n].i - d[n].j

        if n not in d:
            d[n] = Number(i, 0, 1)
        else:
            d[n].j = d[n].i
            d[n].i = i
            d[n].n += 1 
    
    return n

if __name__ == '__main__':
    #data = [0, 3, 6]
    data = [0,1,4,13,15,12,16]
    tick = time.time()
    n = p(data, 2021)
    tock = time.time()
    print(n, ' in ', tock - tick, ' s' )

    tick = time.time()
    n = p(data, 30000001)
    tock = time.time()
    print(n, ' in ', tock - tick, ' s' )


