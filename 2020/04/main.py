expected_fields = (
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        )
        #'cid')

def check_valid(fields):
    for f in fields:
        fid, fva = f.split(':')

        if fid == 'byr':
            if int(fva) < 1920 or int(fva) > 2002 or len(fva) != 4:
                return False
        if fid == 'iyr':
            if int(fva) < 2010 or int(fva) > 2020 or len(fva) != 4:
                return False
        if fid == 'eyr':
            if int(fva) < 2020 or int(fva) > 2030 or len(fva) != 4:
                return False
        if fid == 'hgt':
            if fva[-2:] not in ('in', 'cm'):
                return False
            if fva[-2:] == 'in' and (int(fva[:-2]) < 59 or int(fva[:-2]) > 76):
                return False
            if fva[-2:] == 'cm' and (int(fva[:-2]) < 150 or int(fva[:-2]) > 193):
                return False
        if fid == 'hcl':
            if fva[0] != '#' or len(fva[1:]) != 6 or not fva[1:].isalnum():
                return False
        if fid == 'ecl':
            if fva not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                return False
        if fid == 'pid':
            if len(fva) != 9 or not fva.isdigit():
                return False
    return True


def p1(inputs):
    return sum(all(f in i for f in expected_fields) for i in inputs)

def p2(inputs):
    num_valid = 0
    for i in inputs:
        has_fields = all(f in i for f in expected_fields)
        fields = i.replace('\n', ' ').split()
        if check_valid(fields) and has_fields:
            num_valid += 1

    return num_valid

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        foo = f.read()
        foo = foo.split('\n\n')
        print(p1(foo))
        print(p2(foo))
