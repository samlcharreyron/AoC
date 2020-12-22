from collections import defaultdict

def p1(all_ingreds, d):
    some_als = set()
    for v in d.values():
        some_als |= v
    no_als = all_ingreds.keys() - some_als

    return sum(all_ingreds[ingred] for ingred in no_als)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

        d = dict()
        all_ingreds = defaultdict(int)
        for line in data:
            ingreds, allergens = line.split('(contains')
            allergens = [al.strip() for al in allergens[:-1].split(',')]
            ingreds = ingreds.split()
            for ingred in ingreds:
                all_ingreds[ingred] += 1

            for al in allergens:
                if al not in d:
                    d[al] = set(ingreds)
                else:
                    d[al] &= set(ingreds)

        print(p1(all_ingreds, d))
        while any(len(v) > 1 for v in d.values()):
            remove = {k: cb for k, cb in d.items() if len(cb) ==1}

            for k, v in d.items():
                for kr, vr in remove.items():
                    if k != kr:
                        d[k] -= vr

        print(','.join(d[k].pop() for k in sorted(d.keys())))

