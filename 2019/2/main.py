import sys
from collections import deque

def run_program(line):
    i = 0

    while True:
        c = line[i]
        if c == 99:
            break

        if c == 1:
            i += 1
            i0 = line[i]
            i += 1
            i1 = line[i]
            i += 1
            o = line[i]

            line[o] = line[i0] + line[i1]

            i += 1

        elif c == 2:
            i += 1
            i0 = line[i]
            i += 1
            i1 = line[i]
            i += 1
            o = line[i]

            line[o] = line[i0] * line[i1]

            i +=1
    return line[0]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read()
    line = line.split(',')
    line = [int(c) for c in line] 
    linec = list(line)
    linec[1] = 12
    linec[2] = 2
    print(run_program(linec))

    # p2
    for noun in range(99):
        for verb in range(99):
            linec = list(line)
            linec[1] = noun
            linec[2] = verb
            if run_program(linec) == 19690720:
                print(100 * noun + verb)
                break
