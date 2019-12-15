import cmath
import networkx as nx
import random
from collections import defaultdict, OrderedDict 

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

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()[0]
    line = line.split(',')

    program = Program(line)
    moves = [complex(0,1),complex(0,-1),complex(1,0),complex(-1,0)]
    codes = {complex(0,1):1, complex(0,-1):2, complex(1,0):3, complex(-1,0):4}
    G = nx.Graph()
    p = complex(0,0)
    g = program.run(-1)
    next(g)
    stacks = defaultdict(OrderedDict)
    stacks[p].update({move:0 for move in moves if (p+move) not in G.nodes()})
    while True:
        move, _ = stacks[p].popitem()
        output = g.send(codes[move])
        next(g)
        if output != 0:
            G.add_edge(p, p+move)
            if output == 2:
                dest = p + move
                break
            p += move
            stacks[p].update({move:0 for move in moves if stacks[p+move]}) 
            stacks[p].update({move:0 for move in moves if (p+move) not in G.nodes()})

    print(nx.shortest_path_length(G, complex(0,0), dest)) 
