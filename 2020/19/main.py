import re

def interp(x, d):
    r = ''
    for c in x.split():
        if c[0] == '"' and c[-1] == '"':
            r += c[1:-1]
        elif c == '|':
            r += '|'
        else:
            r += '(' + interp(d[c], d) + ')'
    return r

def get_match(k, d):
    r = r''
    for c in d[k].split():
        r += interp(c, d)
    r += ''
    return r

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        rules, data = f.read().split('\n\n')
        d = dict()
        for line in rules.splitlines():
            n, r = line.split(':')
            d[n] = r.strip()

        r = re.compile(get_match('0', d))
        #print(get_match('1', d))

        print(sum(re.fullmatch(r, line) != None for line in data.splitlines()))
                    
                    

