import numpy as np
from itertools import combinations

def p1(numbers, pre=25):
    for i, n in enumerate(numbers[pre:]):
        if all((a+b) != n for a, b in combinations(numbers[i:(i+pre)], 2)):
            return n

def p2(n, numbers):
    for i in range(len(numbers)):
        cs = np.cumsum(numbers[i:])
        f = np.argwhere(cs == n)
        if f.size > 0:
            r = numbers[i:(i+1+f[0,0])]
            return np.min(r) + np.max(r)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        numbers = [int(n) for n in data]
        n = p1(numbers, 25)
        print(n)
        print(p2(n, numbers))
