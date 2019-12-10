import numpy as np
import itertools
from collections import defaultdict

if __name__ == '__main__':
    data = np.genfromtxt('input.txt', comments='%', dtype=np.character, delimiter=1)
    yv, xv = np.nonzero(data == '#')

    pv = np.stack((xv, yv), axis=1)
    indices = range(len(xv))
    num_ast = np.zeros_like(xv, dtype=int)

    for i in indices:
        rays = pv[list(set(indices) - {i}), :] - pv[i,:]
        angles = np.mod(np.arctan2(rays[:,1], rays[:,0]) + np.pi/2 + 2*np.pi, 2*np.pi)
        num_ast[i] = len(np.unique(angles, axis=0))
    print(max(num_ast))

    # part 2
    im = np.argmax(num_ast)

    others = list(set(indices) - {im})
    rays = pv[others, :] - pv[im, :]
    lengths = np.linalg.norm(rays, axis=1)
    angles = np.mod(np.arctan2(rays[:,1], rays[:,0]) + np.pi/2 + 2*np.pi, 2*np.pi)
    radar = defaultdict(list)
    for angle, other in zip(angles, others):
        radar[angle].append(pv[other,:])

    i = 1
    n = 0
    while sum(len(v) for v in radar.values()):
        #print('it: {}'.format(i))
        for angle in sorted(radar.keys()):
            if radar[angle]:
                p = radar[angle].pop()
                n += 1
                #print('{}: removed {}'.format(n, p))
                if n == 200:
                    print('200: removing {} with code {}'.format(p, 100*p[0]+p[1]))
        i += 1

