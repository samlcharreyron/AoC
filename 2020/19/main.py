import re
import regex

def interp(x, d, p2=False):
    r = ''
    for c in x.split():
        if c[0] == '"' and c[-1] == '"':
            r += c[1:-1]
        elif c == '|':
            r += '|'
        else:
            if p2:
                if c == '8':
                    r += '({})+'.format(interp('42', d))
                elif c == '11':
                    #r += '({}){{1,4}}({}){{1,4}}'.format(interp('42', d), interp('31',d))
                    a = interp('42', d)
                    b = interp('31', d)
                    r +=  '(' + '|'.join(f'{a}{{{n}}}{b}{{{n}}}' for n in range(1, 20)) + ')'
                    #r += '({0}{1})|({0}{{2}}{1}{{2}})'.format(interp('42', d), interp('31', d))
                    #for i in range(2,10):
                    #    r += '|(({}){{{:d}}}({}){{{:d}}})'.format(interp('42', d), i, interp('31', d), i)
            else:
                r += '(' + interp(d[c], d) + ')'
    return r

def p(rules, data, p2=False):
    d = dict()
    for line in rules.splitlines():
        n, r = line.split(':')
        d[n] = r.strip()

    rs = r''
    for c in d['0'].split():
        rs += interp(c, d, p2)
    r = re.compile(rs)

    return sum(re.fullmatch(r, line) != None for line in data.splitlines())

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        rules, data = f.read().split('\n\n')

    print(p(rules, data, False))
    print(p(rules, data, True))
                    
                    

