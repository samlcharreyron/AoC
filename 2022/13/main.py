import ast
import functools

def check(l, r):
    # import ipdb; ipdb.set_trace()
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l > r:
            return 1 
        else:
            return 0 
    elif isinstance(l, list) and isinstance(r, list):
        for ll, rr in zip(l, r):
            if check(ll, rr) == -1:
                # print('l is smaller')
                return -1
            elif check(ll, rr) == 1:
                # print('r is smaller')
                return 1

        if len(l) < len(r):
            # print('l ran out')
            return -1
        elif len(r) < len(l):
            # print('r ran out')
            return 1
        else:
            # print('equal')
            return 0

    elif isinstance(l, list) and isinstance(r, int):
        return check(l, [r])
    else:
        return check([l], r)

if __name__ == '__main__':
    filename = 'input'
    with open(filename, 'r') as f:
        pairs = []
        for pair in f.read().split('\n\n'):
            left = ast.literal_eval(pair.splitlines()[0])
            right = ast.literal_eval(pair.splitlines()[1])
            pairs.append((left, right))

    # for i, (left, right) in enumerate(pairs):
    #     print('pair ', i+1)
    #     print(left)
    #     print(right)
    #     print('right order: ', check(left, right))
    #     print('\n')

    print(sum(i+1 for i, (left, right) in enumerate(pairs) if check(left, right) == -1))
    
    with open(filename, 'r') as f:
        codes = []
        for pair in f.read().split('\n\n'):
            left = ast.literal_eval(pair.splitlines()[0])
            right = ast.literal_eval(pair.splitlines()[1])
            codes.append(left)
            codes.append(right)

    codes.append([[2]])
    codes.append([[6]])
    codes = sorted(codes, key=functools.cmp_to_key(check))
    x, y = [i for i, code in enumerate(codes) if code == [[2]] or code == [[6]]]
    print((x + 1) * (y + 1))
    #for code in codes:
    #    print(code)
