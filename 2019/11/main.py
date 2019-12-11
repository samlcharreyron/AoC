import numpy as np
from collections import defaultdict
import cmath
import matplotlib.pyplot as plt

class Program(object):

    def __init__(self, instruction_list):
        self.i = 0
        self.base = 0
        self.output = -1
        self.instruction_list = list(instruction_list)

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
                return -1

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
                i0 = int(self.instruction_list[self.i+1])
                # put input at i0
                a = self.get_arg_address(i0, pc[0])
                self.instruction_list[a] = str(input_setting)

                self.i += 2
        
            elif oc == 4:
                i0 = int(self.instruction_list[self.i+1])
                # output i0
                a = self.get_arg(i0, pc[0])

                output = a
                #print(output)

                self.i += 2
                return output

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

        return self.output

def rotate(current, instruction):
    if instruction == 1:
        # turn right
        return current + complex(1,0)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        instruction_list = f.read().splitlines()[0]

    instruction_list = instruction_list.split(',')
    instruction_list.extend(['0']*1000)
    
    m = defaultdict(int)
    painted = defaultdict(bool)
    program = Program(instruction_list)

    p = complex(0, 0)
    d = complex(0, 1)
    while True: 
        r = program.run(m[p])
        if r == -1:
            break
        m[p] = r

        painted[p] = True
        s = program.run(-1)
        if s == -1:
            break
        d *= complex(0, 1 - 2*s)
        p += d

    print(len(painted))

    m = defaultdict(int)
    painted = defaultdict(bool)
    program = Program(instruction_list)

    p = complex(0, 0)
    d = complex(0, 1)
    m[p] = 1
    while True: 
        r = program.run(m[p])
        if r == -1:
            break
        m[p] = r

        painted[p] = True
        s = program.run(-1)
        if s == -1:
            break
        d *= complex(0, 1 - 2*s)
        p += d

    xmin = min(p.real for p in m.iterkeys())
    xmax = max(p.real for p in m.iterkeys())
    ymin = min(p.imag for p in m.iterkeys())
    ymax = max(p.imag for p in m.iterkeys())

    img = np.zeros((int(xmax - xmin) + 1, int(ymax - ymin) + 1), np.bool)
    for p, v in m.iteritems():
        x = int(p.real - xmin)
        y = int(p.imag - ymin)
        img[x,y] = v

    plt.imshow(img)
    plt.show()

