from collections import defaultdict, namedtuple

class Number:
    def __init__(self, i, j, n):
        self.i = i
        self.n = n
        self.j = j

    def __repr__(self):
        return 'i: {}, j: {}, n: {}'.format(self.i, self.j, self.n)

if __name__ == '__main__':
    data = [0,1,4,13,15,12,16]
    #data = [0, 3, 6]
    #data = [1, 3, 2]

    d = dict()
    i = 1
    for n in data:
        d[n] = Number(i, 0, 1)
        i += 1

    for i in range(len(data) + 1, 2021):
    #while len(d) < 2020:
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
        #print(i, n)
        #i += 1
    print(n)

