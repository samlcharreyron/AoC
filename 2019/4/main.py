import re

def has_adjacent(x):
    # check for adjacent digits
    for i in range(5):
        ss = str(x)[i:(i+2)]
        if ss[0] == ss[1]:
            return True
    return False

def has_adjacent2(x):
    matches = [match[1] + match[0] for match in re.findall(r'(\d)(\1{1,})', str(x))]
    return 2 in [len(match) for match in matches]

def is_increasing(x):
    return ''.join(sorted(str(x))) == str(x)

if __name__ == '__main__':
    low = 278384
    high = 824795

    candidates = [x for x in range(low, high+1) if has_adjacent(x) and is_increasing(x)]
    print(len(candidates))

    candidates = [x for x in range(low, high+1) if has_adjacent2(x) and is_increasing(x)]
    print(len(candidates))
