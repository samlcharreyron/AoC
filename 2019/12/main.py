import numpy as np
import itertools

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        assert(len(lines) == 4)
    
    positions = []
    for line in lines:
        #line = line.translate(None, '>')
        bits = line.split(',')
        x = int(bits[0][3:])
        y = int(bits[1][3:])
        z = int(bits[2][3:-1])
        positions.append(np.array((x,y,z)))

    velocities = [np.zeros((3,), np.int) for _ in range(4)] 

    for step in range(1000):
        for i, j in itertools.combinations(range(4), 2):
            p1 = positions[i]; p2 = positions[j] 
            v1 = velocities[i]; v2 = velocities[j]
            delp = np.minimum(np.maximum(p2 - p1, -1), 1)
            v1 += delp
            v2 -= delp
            #velocities[i] = v1; velocities[j] = v2
        for p, v in zip(positions, velocities):
            p += v

    print('step: {}'.format(step+1))
    for p,v in zip(positions, velocities):
        print('{} \t{}'.format(p, v))

    # calculating energy
    print(np.sum(np.sum(np.abs(positions), axis=1) * np.sum(np.abs(velocities), axis=1)))
