import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.signal import correlate

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

        acc = 0 
        ic = 0
        ic_l = []
        for _ in range(300):
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
    #plt.plot(ic_l)
    plt.plot(correlate(ic_l, ic_l, mode='same'))
    plt.show()

