import numpy as np
import time
import sys

def print_map(outputs):
    xv = outputs[0:-3:3]
    yv = outputs[1:-3:3]
    tiles = outputs[2:-3:3]
    m = np.zeros((max(yv)+1, max(xv)+1), np.int)
    m[yv, xv] = tiles 
    for r in m:
        for c in r:
            if c == 0:
                sys.stdout.write(' ')
            elif c == 4:
                sys.stdout.write('.')
            elif c == 3:
                sys.stdout.write('_')
            elif c == 2:
                sys.stdout.write('o')
            elif c == 1:
                sys.stdout.write('#')
        sys.stdout.write('\n')

class Program(object):

    def __init__(self, instruction_list):
        self.i = 0
        self.base = 0
        self.output = -1
        self.instruction_list = list(instruction_list)
        self.instruction_list.extend(['0'] * 1000)

    def get_arg(self, i, pc):
        # position mode
        if int(pc) == 0:   
            a = self.instruction_list[i]
        # value mode
        elif int(pc) == 1:
            a = i
        # relative mode
        elif int(pc) == 2:
            a = self.instruction_list[i + self.base]
        else:
            raise ValueError('invalid parameter')

        return int(a)

    def get_arg_address(self, i, pc):
        # position mode
        if int(pc) == 0:   
            a = i
        # relative mode
        elif int(pc) == 2:
            a = i + self.base
        else:
            raise ValueError('invalid parameter')

        return int(a)


    def run(self, input_setting):

        self.output = -1
        outputs = []

        while True:
            code = self.instruction_list[self.i]
            # opcode
            oc = int(code[-2:])

            # param code need to flip to left to right
            if len(code[:-2]):
                pc = '{:03d}'.format(int(code[:-2]))[::-1]
            else:
                pc = '000'

            if oc == 99:
                yield outputs
                break

            if oc == 1:
                i0, i1, o = [int(x) for x in self.instruction_list[(self.i+1):(self.i+4)]]

                a = self.get_arg(i0, pc[0])
                b = self.get_arg(i1, pc[1])
                c = self.get_arg_address(o, pc[2])

                self.instruction_list[c] = str(a + b)

                self.i += 4

            elif oc == 2:
                i0, i1, o = [int(x) for x in self.instruction_list[(self.i+1):(self.i+4)]]

                a = self.get_arg(i0, pc[0])
                b = self.get_arg(i1, pc[1])
                c = self.get_arg_address(o, pc[2])

                self.instruction_list[c] = str(a * b)

                self.i += 4

            elif oc == 3:
                yield outputs
                outputs = []
                i0 = int(self.instruction_list[self.i+1])
                # put input at i0
                a = self.get_arg_address(i0, pc[0])
                #self.instruction_list[a] = str(input_setting)
                joy = yield
                print(joy)
                #self.instruction_list[a] = yield

                self.i += 2
        
            elif oc == 4:
                i0 = int(self.instruction_list[self.i+1])
                # output i0
                a = self.get_arg(i0, pc[0])

                self.output = a
                outputs.append(a)
                #print(output)

                self.i += 2

            elif oc == 5:
                i0, i1 = [int(x) for x in self.instruction_list[(self.i+1):(self.i+3)]]
                a = self.get_arg(i0, pc[0])
                b = self.get_arg(i1, pc[1])

                if a != 0:
                    self.i = b
                else:
                    self.i += 3

            elif oc == 6:
                i0, i1 = [int(x) for x in self.instruction_list[(self.i+1):(self.i+3)]]
                a = self.get_arg(i0, pc[0])
                b = self.get_arg(i1, pc[1])

                if a == 0:
                    self.i = b
                else:
                    self.i += 3

            elif oc == 7:
                i0, i1, o = [int(x) for x in self.instruction_list[(self.i+1):(self.i+4)]]
                a = self.get_arg(i0, pc[0])
                b = self.get_arg(i1, pc[1])
                c = self.get_arg_address(o, pc[2])

                if a < b :
                    self.instruction_list[c] = '1'
                else:
                    self.instruction_list[c] = '0'

                self.i += 4

            elif oc == 8:
                i0, i1, o = [int(x) for x in self.instruction_list[(self.i+1):(self.i+4)]]
                a = self.get_arg(i0, pc[0])
                b = self.get_arg(i1, pc[1])
                c = self.get_arg_address(o, pc[2])

                if a == b:
                    self.instruction_list[c] = '1'
                else:
                    self.instruction_list[c] = '0'

                self.i += 4

            elif oc == 9:
                i0 = int(self.instruction_list[self.i+1])
                a = self.get_arg(i0, pc[0])
                # put input at i0
                self.base += a 

                self.i += 2

            #self.steps += 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()[0]
    line = line.split(',')

    program = Program(line)

    tiles = []
    g = program.run(-1)
    outputs = next(g)
    xv = outputs[0::3]
    yv = outputs[1::3]
    tiles = outputs[2::3]
    print(sum(t ==2 for t in tiles))
    m = np.zeros((max(yv)+1, max(xv)+1), np.int)

    # part 2
    line[0] = '2'
    program = Program(line)
    g = program.run(0)
    while True:
        outputs = next(g)
        import pdb; pdb.set_trace()
        print_map(outputs)
        xv = outputs[0:-3:3]
        yv = outputs[1:-3:3]
        tiles = outputs[2:-3:3]

        score = outputs[-1]
        print('score: {}'.format(score))

        # ball position
        xb , yb = [(x,y) for x, y, t in zip(xv, yv, tiles) if t ==4][0]
        # paddle position
        xp , yp = [(x,y) for x, y, t in zip(xv, yv, tiles) if t ==3][0]
        j = min(max(xb - xp, -1), 1)

        g.send(j)


    

