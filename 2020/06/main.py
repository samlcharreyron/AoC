from functools import reduce

def p1(entries):
    return sum(len(set(''.join(g))) for g in entries)

def p2(entries):
    return sum(len(reduce(set.intersection, (set(''.join(p)) for p in g))) 
            for g in entries)
    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        entries = [[]]
        i = 0
        for line in lines:
            x = line.strip()
            if not x:
                entries.append([])
                i += 1
            else:
                entries[i].append(x)
        print(p1(entries))
        print(p2(entries))
