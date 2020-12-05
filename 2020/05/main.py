import numpy as np
import matplotlib.pyplot as plt

def process_bp(bp):
    cur = range(0, 128)

    for c in bp[0:-3]:
        if c == 'F':
            cur = range(cur.start, int((cur.start + cur.stop)/2))
        else:
            cur = range(int((cur.start + cur.stop)/2), cur.stop)
    row = cur.start

    cur = range(0, 8)
    for c in bp[-3:]:
        if c == 'L':
            cur = range(cur.start, int((cur.start + cur.stop)/2))
        else:
            cur = range(int((cur.start + cur.stop)/2), cur.stop)
    col = cur.stop - 1
    return row * 8 + col

def p1(lines):
    return max(process_bp(bp) for bp in lines)

def p2(lines):
    seats = [process_bp(bp) for bp in lines]
    seats.sort()
    for x, y in zip(seats, seats[1::]):
        if (y - x) == 2:
            return x + 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().split()
    print(p1(lines))
    print(p2(lines))
