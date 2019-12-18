import numpy as np
from collections import defaultdict, OrderedDict
import cmath
import networkx as nx
from scipy.spatial import cKDTree

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        lines = f.read().splitlines()
    
    m = dict()
    doors = dict()
    keys = dict()
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == '@':
                start = complex(i,j)
                m[start] = '.'
            elif c.isupper():
                doors[c.lower()] = complex(i,j)
                m[complex(i,j)] = c
            elif c.islower():
                keys[c] = complex(i,j)
                m[complex(i,j)] = c
            else:
                m[complex(i,j)] = c

    moves = [complex(1,0), complex(-1,0), complex(0,1), complex(0,-1)]
    pos = start

    G = nx.Graph()
    data = np.array([np.array([k.real, k.imag]) for k,v in m.items() if v != '#' and not v.isupper()])
    tree = cKDTree(data) 

    for i,j in tree.query_pairs(r=1):
        G.add_edge(complex(data[i,0], data[i,1]), complex(data[j,0], data[j,1]))

    all_keys_sorted = dict()
    path_lengths = {k:nx.shortest_path_length(G, pos, v) for k,v in keys.items() if nx.has_path(G, pos, v)}
    keys_sorted = OrderedDict(sorted(path_lengths.items(), reverse=True, key=lambda kv: kv[1]))
    #all_keys_sorted[pos] = keys_sorted

    J = dict()
    node = 's'
    total_length = 0
    remaining_keys = keys.keys()
    stacks = defaultdict(set)
    stacks[node] = set(k for k,v in keys.items() if nx.has_path(G, pos, v))
    import pdb; pdb.set_trace()
    while stacks:
        if not stacks[node]:
            print('reached bottom')
            J[node] = 0
            node = node[:-1]
            continue

        k = stacks[node].pop()
        prev = node
        node += k
        l = nx.shortest_path_length(G, pos, keys[k])

        if node in J.keys():
            costs[prev][node] =  l + J[node]
            continue

        pos = keys[k]
        remaining_keys -= set(k)

        print('collecting', k, 'has left', remaining_keys)
        if k in doors.keys():
            print('unlocking', k.upper())
            door = doors[k]
            for i in tree.query_ball_point([door.real, door.imag], 1):
                G.add_edge(door, complex(data[i,0], data[i,1]))
        stacks[node] = set(k for k in remaining_keys if nx.has_path(G, pos, keys[k]))

    print(d)
