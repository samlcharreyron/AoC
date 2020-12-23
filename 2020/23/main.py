from collections import deque
from bisect import bisect_left

if __name__ == '__main__':
    #data = '389125467'
    data = '624397158'

    q = deque(int(c) for c in data)

    for i in range(1, 101):
        q.rotate(-1)
        c1 = q.popleft()
        c2 = q.popleft()
        c3 = q.popleft()
        q.rotate(1)
        c = q[0]
        qs = sorted(list(q))
        didxs = bisect_left(qs, c - 1)
        #import pdb; pdb.set_trace()

        if didxs == 0: 
            if qs[0] != (c-1):
                d = qs[-1]
            else:
                d = qs[0]
        else:
            if qs[didxs] == (c-1):
                d = c - 1
            else:
                d = qs[didxs - 1]

        didx = q.index(d)
        q.rotate((-didx - 1))
        q.extendleft([c3, c2, c1])
        q.rotate(didx + 1)
            
        q.rotate(-1)
        #print(i, d, q)

    idx = q.index(1)
    q.rotate(-idx)
    q.popleft()
    print(''.join(str(c) for c in q))
