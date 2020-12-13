def p1(e, ls):
    t = e
    while True:
        for l in ls:
            if (t % l) == 0:
                return (t - e) * l
        t += 1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        e = int(data[0])
        ls = [int(l) for l in data[1].split(',') if l != 'x']
        print(p1(e, ls))

