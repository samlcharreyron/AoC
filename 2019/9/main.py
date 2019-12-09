
def get_arg(line, i, pc):
    global base
    # position mode
    if int(pc) == 0:   
        a = line[i]
    # value mode
    elif int(pc) == 1:
        a = i
    # relative mode
    elif int(pc) == 2:
        a = line[i + base]
    else:
        raise ValueError('invalid parameter')

    return int(a)

def get_arg_address(line, i , pc):
    global base
    # position mode
    if int(pc) == 0:   
        a = i
    # relative mode
    elif int(pc) == 2:
        a = i + base
    else:
        raise ValueError('invalid parameter')

    return int(a)

def run_program(line, input_setting):
    global base

    output = -1
    i = 0
    base = 0

    while i < len(line):
        code = line[i]
        # opcode
        oc = int(code[-2:])

        # param code need to flip to left to right
        if len(code[:-2]):
            pc = '{:03d}'.format(int(code[:-2]))[::-1]
        else:
            pc = '000'

        if oc == 99:
            return output

        if oc == 1:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]

            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])
            c = get_arg_address(line, o, pc[2])

            line[c] = str(a + b)

            i += 4

        elif oc == 2:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]

            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])
            c = get_arg_address(line, o, pc[2])

            line[c] = str(a * b)

            i += 4

        elif oc == 3:
            i0 = int(line[i+1])
            # put input at i0
            a = get_arg_address(line, i0, pc[0])
            line[a] = str(input_setting)

            i += 2
    
        elif oc == 4:
            i0 = int(line[i+1])
            # output i0
            a = get_arg(line, i0, pc[0])

            output = a
            print(output)

            i += 2

        elif oc == 5:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])

            if a != 0:
                i = b
            else:
                i += 3

        elif oc == 6:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])

            if a == 0:
                i = b
            else:
                i += 3

        elif oc == 7:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])
            c = get_arg_address(line, o, pc[2])

            if a < b :
                line[c] = '1'
            else:
                line[c] = '0'

            i += 4

        elif oc == 8:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])
            c = get_arg_address(line, o, pc[2])

            if a == b:
                line[c] = '1'
            else:
                line[c] = '0'

            i += 4

        elif oc == 9:
            i0 = int(line[i+1])
            a = get_arg(line, i0, pc[0])
            # put input at i0
            base += a 

            i += 2

    return output

if __name__ == '__main__':
    # with open('test2.txt', 'r') as f:
        # line = f.read().splitlines()[0]
    # line = line.split(',')
    # # pad the program
    # line.extend(['0']*1000)
    # #print(line)
    # run_program(list(line), 0)
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()[0]
    line = line.split(',')
    # pad the program
    line.extend(['0']*1000)
    run_program(line, 1)
