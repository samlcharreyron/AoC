def get_arg(line, i, pc):
    # position mode
    if not int(pc[0]):   
        a = line[i]
    else:
        a = i

    return int(a)

def run_program(line, in_code):

    # do first part
    line[int(line[1])] = str(in_code)

    i = 2

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
            break


        if oc == 1:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]

            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])

            line[o] = str(a + b)

            i += 4

        elif oc == 2:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]

            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])

            line[o] = str(a * b)

            i += 4

        elif oc == 3:
            i0 = int(line[i+1])
            a = get_arg(line, i0, pc[0])
            # put input at i0
            line[i0] = str(a)

            i += 2
    
        elif oc == 4:
            i0 = int(line[i+1])
            # output i0
            a = get_arg(line, i0, pc[0])
            print a

            i += 2

        elif oc == 5:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])
            if a != 0:
                i = b
                #i = i1
            else:
                i += 3

        elif oc == 6:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])
            if a == 0:
                i = b
                #i = i1
            else:
                i += 3

        elif oc == 7:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])

            if a < b :
                line[o] = '1'
            else:
                line[o] = '0'
            i += 4

        elif oc == 8:
            i0, i1, o = [int(x) for x in line[(i+1):(i+4)]]
            a = get_arg(line, i0, pc[0])
            b = get_arg(line, i1, pc[1])

            if a == b:
                line[o] = '1'
            else:
                line[o] = '0'
            i += 4

    return line[0]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()[0]
    line = line.split(',')
    run_program(list(line), 1)
    run_program(list(line), 5)


