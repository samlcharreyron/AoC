import sys
from collections import defaultdict

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    occupancy = defaultdict(int)
    step_count = defaultdict(int)
    for line in lines:
        steps = line.split(',')
        x = 0
        y = 0

        # this one the occupancy of a single wire
        o = defaultdict(int)
        s = 0
        for step in steps:
            num = int(step[1:])
            if step[0] == 'R':
                for k in range(num):   
                    x += 1
                    s += 1
                    o[(x,y)] = s

            if step[0] == 'L':
                for k in range(num):  
                    x -= 1
                    s += 1
                    o[(x,y)] = s

            if step[0] == 'U':
                for k in range(num):  
                    y += 1
                    s += 1
                    o[(x,y)] = s 

            if step[0] == 'D':
                for k in range(num):  
                    y -= 1
                    s += 1
                    o[(x,y)] = s 

        # merge occupancies
        for k, s in o.iteritems():
            occupancy[k] += 1
            step_count[k] += s

    #print occupancy
    distances = [abs(x) + abs(y) for (x, y) , v in occupancy.iteritems() if v > 1]
    print(min(distances))

    # counting steps
    print(min(step_count[k] for k, v in occupancy.iteritems() if v > 1))
