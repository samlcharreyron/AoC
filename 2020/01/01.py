import itertools
import math
import time
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()   

        entries = [int(line.strip()) for line in lines]

        
        start = time.time()
        print(math.prod([comb for comb in itertools.combinations(entries, 2) if sum(comb) == 2020][0]))
        end = time.time()
        print('took {} us'.format(1e6*(end - start)))

        start = time.time()
        print(math.prod([comb for comb in itertools.combinations(entries, 3) if sum(comb) == 2020][0]))
        end = time.time()
        print('took {} us'.format(1e6*(end - start)))
