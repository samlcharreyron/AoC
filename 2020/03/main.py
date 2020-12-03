from collections import defaultdict
import math

def build_map(lines):
    m = defaultdict(int)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#': 
                m[complex(x, y)] = 1
            else:
                m[complex(x, y)] = 0
    return m

def gen_p1(m, w, h, dp):
    p = complex(0, 0)

    while p.imag < h:
        p =  (p + dp)
        p = complex(p.real % w, p.imag)
        yield m[p]

def p1(m, w, h, dp=complex(3, 1)):
    return sum(t for t in gen_p1(m, w, h, dp))

def p2(m, w, h):
    slopes = [complex(1, 1), complex(3, 1), complex(5, 1), complex(7, 1),
            complex(1, 2)]
    return math.prod(p1(m, w, h, dp) for dp in slopes)
        

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        h = len(lines)
        w = len(lines[0])
        m = build_map(lines)

        print(p1(m, w, h))
        print(p2(m, w, h))
