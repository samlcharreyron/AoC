from math import pi, radians, cos, sin, sqrt

def p1(data):
    drs = {       
            'E': complex(1, 0),
            'W': complex(-1, 0),
            'N': complex(0, 1),
            'S': complex(0, -1)
            }

    ans = {
            -270 : complex(0, 1),
            -180: complex(-1, 0),
            -90 : complex(0, -1),
            0 : complex(1, 0),
            90 : complex(0, 1),
            180: complex(-1, 0),
            270: complex(0, -1),
            }

    d = drs['E']
    p = complex(0, 0)

    for line in data:
        i = line[0]
        n = int(line[1:])
        if i in drs.keys():
            p += n * drs[i]
        elif i  == 'L':
            d *= ans[n]
        elif i == 'R':
            d *= ans[-n]
        elif i == 'F':
            p += n * d
    return round(abs(p.real) + abs(p.imag))

def p2(data):
    drs = {       
            'E': complex(1, 0),
            'W': complex(-1, 0),
            'N': complex(0, 1),
            'S': complex(0, -1)
            }

    ans = {
            -270 : complex(0, 1),
            -180: complex(-1, 0),
            -90 : complex(0, -1),
            0 : complex(1, 0),
            90 : complex(0, 1),
            180: complex(-1, 0),
            270: complex(0, -1),
            }

    wp = complex(10, 1)
    sp = complex(0, 0)

    for line in data:
        i = line[0]
        n = int(line[1:])
        if i in drs.keys():
            wp += n * drs[i]
        elif i  == 'L':
            wp *= ans[n]
        elif i == 'R':
            wp *= ans[-n]
        elif i == 'F':
            sp += n * wp 

    return round(abs(sp.real) + abs(sp.imag))

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    print(p1(data))
    print(p2(data))



