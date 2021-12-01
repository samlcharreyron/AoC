from functools import reduce

def p1(entries):
    return sum(len(set(''.join(g))) for g in entries)

def p2(entries):
    return sum(len(reduce(set.intersection, (set(''.join(p)) for p in g))) 
            for g in entries)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().strip().split('\n\n')
        entries = [d.split('\n') for d in data]
        print(p1(entries))
        print(p2(entries))
