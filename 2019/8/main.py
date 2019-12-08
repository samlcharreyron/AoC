import numpy as np
import matplotlib.pyplot as plt

def get_image(filename, width, height):
    with open(filename, 'r') as f:
        line = f.read().splitlines()[0]

    d = np.array(list(line)).astype(np.int)
    layers = len(d) / (width * height)

    d = d.reshape((layers, height, width))
    return d

if __name__ == '__main__':

    d = get_image('input.txt', 25, 6)
    l = np.argmin(np.sum(d == 0, axis=(1,2)))
    print(np.sum(d[l,:,:] == 1) * np.sum(d[l,:,:] == 2))

    #d = get_image('test.txt', 2, 2)

    # dirty method
    output = np.zeros(d.shape[1:], np.int)
    for i in xrange(d.shape[1]):
        for j in xrange(d.shape[2]):
            # get first opaque
            l = np.argmax(d[:,i,j] != 2)
            output[i, j] = d[l,i,j]
    plt.imshow(output)
    plt.show()


