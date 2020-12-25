#import numpy as np
#import matplotlib.pyplot as plt

def handshake(sn, ls):
    #value = 1
    #for _ in range(ls):
    #    value *= sn
    #    value = value % 20201227
    #return value
    return pow(sn, ls, 20201227)

def crack(k):
    ln = 0
    k_ = -1
    while k_ != k:
        ln += 1
        k_ = handshake(7, ln)
    return ln

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        ck, dk = (int(line) for line in f.read().splitlines())

        #x = np.arange(0, 100)
        #plt.plot(handshake(7,x))
        #plt.show()

        #dln = crack(dk)
        #cln = crack(ck)
        #print(dln, cln) 

        dln = 6662323
        dcn = 4618530

        print(handshake(ck, dln))
        print(handshake(dk, cln))
