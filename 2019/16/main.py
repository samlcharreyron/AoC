import numpy as np
import math
import scipy.fftpack
import time

def compute(digits, base_pattern, i):
    pattern = np.repeat(base_pattern, i+1)
    pattern = np.roll(pattern, i)
    pattern = pattern[0:len(digits)]
    return np.abs(np.sum(digits * pattern)) % 10

def compute3(digits, base_pattern, offset, r):
    Nd = len(digits)
    N = Nd * r
    rmd = offset % Nd
    repeating = np.tile(digits, r - math.ceil(offset / Nd))
    a = np.hstack((digits[rmd:], repeating))
    Na = len(a)

    tick = time.perf_counter()
    pattern = np.repeat(base_pattern, offset+1)
    tock = time.perf_counter()
    import pdb; pdb.set_trace()
    patternl = np.tile(pattern, math.ceil(Na / len(pattern)))
    b = patternl[:Na]
    print('elapsed setup', tock - tick)

    return np.abs(np.sum(a * b)) % 10

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()[0]

    digits = np.array([int(c) for c in line])
    N = len(digits)

    #base_pattern = np.tile([1,0,-1,0], math.ceil(len(digits)/4))
    base_pattern = np.array([1,0,-1,0])
    # out = list(digits)
    # for _ in range(100):
       # out = [compute(out, base_pattern, i) for i in range(N)]
    # print(''.join(str(c) for c in out[:8]))

    # part 2
    repeats  = 10000 
    offset = int(line[:7])
    print(offset)
    N = len(digits) * repeats
    out = list(digits)
    tick = time.perf_counter()
    out = compute3(out, base_pattern, N-1, repeats) 
    tock = time.perf_counter()
    print('elapsed', tock - tick)
    # for _ in range(1):
        # out = [compute3(out, base_pattern, i) for i in range(offset, N)]

