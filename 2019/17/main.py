import numpy as np
import scipy.signal
import networkx as nx
from scipy.spatial import cKDTree
#import matplotlib.pyplot as plt

class Program(object):

    def __init__(self, instruction_list):
        self.i = 0
        self.base = 0
        self.output = -1
        self.instruction_list = list(instruction_list)
        self.instruction_list.extend(['0'] * 30000)

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
                outputs = []
                i0 = int(self.instruction_list[self.i+1])
                # put input at i0
                a = self.get_arg_address(i0, pc[0])
                joy = yield
                self.instruction_list[a] = joy

                self.i += 2
        
            elif oc == 4:
                i0 = int(self.instruction_list[self.i+1])
                # output i0
                a = self.get_arg(i0, pc[0])

                self.output = a
                yield a

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

def conv(x):
    if x in '^#':
        return 1
    elif x == '.':
        return 0
    else:
        raise ValueError

def get_path_code(path):
    direction = complex(0,-1)
    prev = path[0]
    code = []
    for new in path[1:]:
        dp = new - prev
        prev = new
        if direction != dp:
            # what about case where need to rotate 180
            if int((dp / direction).imag) == 1:
                code.append('R')
                direction *= complex(0,1)
            else:
                code.append('L')
                direction *= complex(0,-1)
            code.append(1)
        else:
            code[-1] += 1
    return code

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()[0]

    line = line.split(',')
    program = Program(line)

    g = program.run(-1)
    outputs = ''.join(chr(output) for output in g)
    #print(outputs)
    # find starting post
    m = np.array([[c for c in line] for line in outputs.splitlines()[:-1]])
    yv, xv = np.where(m=='^')
    start = complex(xv[0], yv[0])
    orientation = complex(0, 1)
    m = np.array([[conv(c) for c in line] for line in outputs.splitlines()[:-1]])
    corner = np.array([[0,1,0],[1,1,1], [0,1,0]], np.int)
    mask = scipy.signal.convolve2d(m, corner)
    yv,xv = np.where(mask == 5)
    print(sum((x-1) * (y-1) for x, y in zip(xv, yv)))

    G = nx.Graph()
    yv, xv = np.where(m==1)
    tree = cKDTree(np.stack((xv, yv), axis=1))

    for i,j in tree.query_pairs(r=1):
        G.add_edge(complex(xv[i], yv[i]), complex(xv[j], yv[j]))
    # find end
    end = set([k for k, v in nx.degree(G) if v < 2]).difference(set([start])).pop()
    
    print([len(path) for path in nx.node_disjoint_paths(G, start, end)])
    long_path = max((path for path in nx.all_simple_paths(G, start, end)),
                    key=lambda path: len(path))
    code = get_path_code(long_path)
    print(code)


