import numpy as np
import matplotlib.pyplot as plt
#from scipy.fft import fft

if __name__ == '__main__':
    with open('input2.txt', 'r') as f:
        data = f.read().splitlines()

        acc = 0 
        ic = 0
        ic_l = []
        for _ in range(1000):
            print(ic, acc, data[ic])
            inst, num = data[ic].split()
            num = int(num)

            if inst == 'acc':
                acc += num
                ic += 1
            elif inst == 'jmp':
                ic += num
            elif inst == 'nop':
                ic += 1
            else:
                raise ValueError('invalid instruction')

            if ic >= len(data):
                break

            ic_l.append(ic)
