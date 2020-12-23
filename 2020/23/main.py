
def play(data, is_p2=False):
    q = [int(c) for c in data]

    if is_p2:
        q.extend(range(max(q)+1,1000001))

    qs = sorted(q)

    ll = dict()
    for c, cn in zip(q, q[1:]):
        ll[c] = cn

    ll[q[-1]] = q[0]

    if is_p2:
        ur = 10000001
    else:
        ur = 101

    c = q[0]

    for i in range(1, ur):
        c1 = ll[c]
        c2 = ll[c1]
        c3 = ll[c2]

        ll[c] = ll[c3]

        di = c - 2
        d = qs[di]

        while d in (c1, c2, c3):
            di -= 1
            d = qs[di]

        ll[c3] = ll[d]
        ll[d] = c1
        #print(d, c1, c2, c3, ll)

        c = ll[c]

    if is_p2:
        d = ll[1]
        return d * ll[d]
    else:
        c = 1
        q = []
        for _ in range(len(ll)-1):
            c = ll[c]
            q.append(c)
        return ''.join(str(c) for c in q)

if __name__ == '__main__':
    #data = '389125467'
    data = '624397158'
    print(play(data))
    print(play(data, is_p2=True))
