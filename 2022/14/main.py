from collections import defaultdict, Counter
import copy

def print_map(m, xmin, xmax, ymin, ymax):
    for y in range(ymin, ymax+1):
        s = ''
        for x in range(xmin, xmax+1):
            s += m[complex(x, y)]
        print(s)

def part1(m):
    rounds = 913 
    for _ in range(rounds):
        st = [start + 1j] 
        while st:
            c = st.pop()
            d = c + 1j
            dl = c + (-1 + 1j)
            dr = c + (1 + 1j)
            if m[d] in 'o#' and m[dl] in 'o#' and m[dr] in 'o#':
                m[c] = 'o'
                #print_map(m)
                continue

            if m[d] in 'o#':
                if m[dl] not in 'o#':
                    st.append(dl)
                elif m[dr] not in 'o#':
                    st.append(dr)
            else:
                st.append(d)

    
    xmax = int(max(p.real for p in m.keys())) 
    xmin = int(min(p.real for p in m.keys()))
    ymax = int(max(p.imag for p in m.keys()))
    ymin = int(min(p.imag for p in m.keys()))
    print_map(m, xmin, xmax, ymin, ymax)
    
    print(rounds)

def part2(m):
    ymax = int(max(p.imag for p in m.keys()))
    padding = ymax + 2

    for j in range(padding + 1):
        m[complex(500 - j, ymax + 2)] = '#'
        m[complex(500 + j, ymax + 2)] = '#'

    rounds = 32000 
    for _ in range(rounds):
        st = [start] 
        while st:
            c = st.pop()
            d = c + 1j
            dl = c + (-1 + 1j)
            dr = c + (1 + 1j)
            if m[d] in 'o#' and m[dl] in 'o#' and m[dr] in 'o#':
                m[c] = 'o'
                #print_map(m)
                continue

            if m[d] in 'o#':
                if m[dl] not in 'o#':
                    st.append(dl)
                elif m[dr] not in 'o#':
                    st.append(dr)
            else:
                st.append(d)

    
    xmax = int(max(p.real for p in m.keys())) 
    xmin = int(min(p.real for p in m.keys()))
    ymax = int(max(p.imag for p in m.keys()))
    ymin = int(min(p.imag for p in m.keys()))
    print_map(m, xmin, xmax, ymin, ymax)
    
    print(Counter(m.values())['o'])
    #print(rounds)

if __name__ == '__main__':
    with open('test') as f:
        lines = f.readlines()

    m = defaultdict(lambda: '.')
    for line in lines:
        vals = [x.strip().split(',') for x in line.split('->')]
        positions = []
        for val in vals:
            x, y = val
            positions.append(complex(int(x), int(y)))

        for s, e in zip(positions, positions[1::]):
            dist = int(abs(e -s))
            dir = (e - s) / dist
            for j in range(dist + 1):
                m[s + j * dir] = '#'

    start = complex(500, 0)
    m[start] = '+'

    #part1(copy.deepcopy(m))
    part2(copy.deepcopy(m))
    
