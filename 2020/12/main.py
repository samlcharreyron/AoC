import math
import cmath

def p1(data):
    drs = {       
            'E': complex(1, 0),
            'W': complex(-1, 0),
            'N': complex(0, 1),
            'S': complex(0, -1)
            }

    d = drs['E']
    p = complex(0, 0)

    for line in data:
        i = line[0]
        n = int(line[1:])
        if i in drs.keys():
            p += n * drs[i]
        elif i  == 'L':
            d *= cmath.rect(1, n * math.pi/180)
        elif i == 'R':
            d *= cmath.rect(1, -n * math.pi/180)
        elif i == 'F':
            p += n * d
    return abs(p.real) + abs(p.imag)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    print(p1(data))



