def f(sub):
    r = int(sub[-1])
    o = sub[-2]

    if len(sub) == 3:
        if o == '+':
            return r + int(sub[0])
        else:
            return r * int(sub[0])
    else:
        if o == '+':
            return r + f(sub[:-2])
        else:
            return r * f(sub[:-2])

def evalu(data):
    while '(' in data:
        s = []
        subs = []
        t = 0
        for i, c in enumerate(data):
            if c == '(':
                s.append(i)
            elif c == ')':
                b = s.pop()
                subs.append((b, i))

        data_ = data
        for s, e in subs:
            sub = data[s+1:e].split() 
            if '(' not in ''.join(sub):
                data_ = data_.replace(data[s:e+1], '{}'.format(f(sub)))
        data = data_
    return f(data.split())

if __name__ == '__main__':
    #data = '1 + 2 * 3 + 4 * 5 + 6'
    #data = '2 * 3 + (4 * 5)'
    #data = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    with open('input.txt', 'r') as fe:
        data = fe.read().splitlines()
    print(sum(evalu(line) for line in data))
