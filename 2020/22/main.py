from collections import deque 
from itertools import islice

def get_score(d):
    return sum(m * c for m, c in zip(range(len(d), 0, -1), d))

def p1(d1, d2):
    while(len(d1) > 0 and len(d2) > 0):
        c1 = d1.popleft()
        c2 = d2.popleft()
        if c1 > c2:
            d1.extend([c1, c2])
        else:
            d2.extend([c2, c1])

    if len(d1) > 0:
        print('Player 1 wins')
        print(get_score(d1))
    else:
        print('Player 2 wins')
        print(get_score(d2))

def p2(d1, d2):
    h1 = set()
    h2 = set()
    r = 0 
    while len(d1) > 0 and len(d2) > 0:
        if tuple(d1) in h1 or tuple(d2) in h2:
            return True, get_score(d1)
        else:
            r += 1

            h1.add(tuple(d1))
            h2.add(tuple(d2))

            c1 = d1.popleft()
            c2 = d2.popleft()

            if len(d1) >= c1 and len(d2) >= c2:
                p1_win, score = p2(deque(islice(d1.copy(), 0, c1)),
                        deque(islice(d2.copy(), 0, c2)))

                if p1_win:
                    d1.extend([c1, c2])
                else:
                    d2.extend([c2, c1])

            else:
                if c1 > c2:
                    d1.extend([c1, c2])
                else:
                    d2.extend([c2, c1])
                #print(c1, c2, d1, d2)

    if len(d1) > 0:
        return True, get_score(d1)
    else:
        return False, get_score(d2)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read()

        d1, d2 = (p.splitlines()[1:] for p in data.split('\n\n'))
        d1 = deque(int(c) for c in d1)
        d2 = deque(int(c) for c in d2)

        #p1(d1, d2)
        print(p2(d1, d2))

