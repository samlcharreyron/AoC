import itertools

def get_arg(line, i, pc):
    # position mode
    if not int(pc[0]):   
        a = line[i]
    else:
        a = i

    return int(a)

def run_program(line, phase, input_setting):

    output = -1

    # get phase setting
    line[int(line[1])] = str(phase)

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
            return output

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
            line[i0] = str(input_setting)

            i += 2
    
        elif oc == 4:
            i0 = int(line[i+1])
            # output i0
            a = get_arg(line, i0, pc[0])
            #print a

            output = a

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

class Program(object):

    def __init__(self, pid, phase, instructions):
        self.id = pid
        self.phase = phase
        self.instructions = instructions
        self.is_phase_set = False
        self.is_done = False
        self.i = 0

    def set_input(self, input_setting):
        self.input_setting = input_setting

    def run_program(self):
        output = -1

        if not self.is_phase_set:
            # get phase setting
            self.instructions[int(self.instructions[1])] = str(self.phase)

            self.i = 2
            self.is_phase_set = True

        while self.i < len(self.instructions):
            code = self.instructions[self.i]
            # opcode
            oc = int(code[-2:])

            # param code need to flip to left to right
            if len(code[:-2]):
                pc = '{:03d}'.format(int(code[:-2]))[::-1]
            else:
                pc = '000'

            if oc == 99:
                self.is_done = True
                #print('program {} is done'.format(self.id))
                return -1

            if oc == 1:
                i0, i1, o = [int(x) for x in self.instructions[(self.i+1):(self.i+4)]]

                a = get_arg(self.instructions, i0, pc[0])
                b = get_arg(self.instructions, i1, pc[1])

                self.instructions[o] = str(a + b)

                self.i += 4

            elif oc == 2:
                i0, i1, o = [int(x) for x in self.instructions[(self.i+1):(self.i+4)]]

                a = get_arg(self.instructions, i0, pc[0])
                b = get_arg(self.instructions, i1, pc[1])

                self.instructions[o] = str(a * b)

                self.i += 4

            elif oc == 3:
                i0 = int(self.instructions[self.i+1])
                a = get_arg(self.instructions, i0, pc[0])
                # put input at i0
                self.instructions[i0] = str(self.input_setting)

                self.i += 2
        
            elif oc == 4:
                i0 = int(self.instructions[self.i+1])
                # output i0
                a = get_arg(self.instructions, i0, pc[0])

                output = a

                self.i += 2

                return output

            elif oc == 5:
                i0, i1, o = [int(x) for x in self.instructions[(self.i+1):(self.i+4)]]
                a = get_arg(self.instructions, i0, pc[0])
                b = get_arg(self.instructions, i1, pc[1])
                if a != 0:
                    self.i = b
                else:
                    self.i += 3

            elif oc == 6:
                i0, i1, o = [int(x) for x in self.instructions[(self.i+1):(self.i+4)]]
                a = get_arg(self.instructions, i0, pc[0])
                b = get_arg(self.instructions, i1, pc[1])
                if a == 0:
                    self.i = b
                else:
                    self.i += 3

            elif oc == 7:
                i0, i1, o = [int(x) for x in self.instructions[(self.i+1):(self.i+4)]]
                a = get_arg(self.instructions, i0, pc[0])
                b = get_arg(self.instructions, i1, pc[1])

                if a < b :
                    self.instructions[o] = '1'
                else:
                    self.instructions[o] = '0'
                self.i += 4

            elif oc == 8:
                i0, i1, o = [int(x) for x in self.instructions[(self.i+1):(self.i+4)]]
                a = get_arg(self.instructions, i0, pc[0])
                b = get_arg(self.instructions, i1, pc[1])

                if a == b:
                    self.instructions[o] = '1'
                else:
                    self.instructions[o] = '0'
                self.i += 4

if __name__ == '__main__':
    # with open('input.txt', 'r') as f:
        # line = f.read().splitlines()[0]
    # line = line.split(',')
    # #phase_settings = (4, 3, 2, 1, 0)
    # #phase_settings = (0, 1, 2, 3, 4)
    # phase_settings = (1, 0, 4, 3, 2)
    # #o = 0
    # #for phase in phase_settings:
    # #    o = run_program(list(line), phase, o)
    # #print(o)
    # output_codes = []
    # for phase_settings in itertools.permutations([0,1,2,3,4]):
        # output = 0
        # for phase in phase_settings:
            # output = run_program(list(line), phase, output)
        # output_codes.append(output)
    # print(max(output_codes))

    # part 2
    with open('input.txt', 'r') as f:
        line = f.read().splitlines()[0]
    line = line.split(',')
    phase_settings = (9,7,8,5,6)
    output_codes = []

    for phase_settings in itertools.permutations([5,6,7,8,9]):
        # first create amplifiers
        programs = [Program(i, phase, list(line)) for i, phase in enumerate(phase_settings)]
        output = 0
        running_programs = ([program for program in programs if not program.is_done])
        while any(running_programs):
            for program in running_programs:
                program.set_input(output)
                temp = program.run_program()
                if not program.is_done:
                    output = temp
            running_programs = ([program for program in programs if not program.is_done])
        output_codes.append(output)
    print(max(output_codes))
