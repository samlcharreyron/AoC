import numpy as np
from collections import defaultdict, OrderedDict
import cmath
import networkx as nx
from scipy.spatial import cKDTree
import itertools
import matplotlib.pyplot as plt

def find_path(c1, c2):
    if not nx.has_path(G, keys_and_doors[c1], keys_and_doors[c2]):
        raise ValueError('no path')

    path = nx.shortest_path(G, keys_and_doors[c1], keys_and_doors[c2])

    blocks = [m[p] for p in path[1:-1] if m[p].isupper()]

    if c2.upper() in blocks:
        raise ValueError('no path that is not blocking')

    if blocks:
        door = blocks[0]
        block_k = door.lower()
        return find_path(c1, block_k) + find_path(block_k, door) + find_path(door, c2)
    else:
        return [(c1, c2, len(path))]

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        lines = f.read().splitlines()
    
    m = dict()
    doors = dict()
    #keys = dict()
    keys_and_doors = dict()
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == '@':
                start = complex(i,j)
                m[start] = '.'
                keys_and_doors[c] = complex(i,j)
            elif c.isupper():
                keys_and_doors[c] = complex(i,j)
                m[complex(i,j)] = c
            elif c.islower():
                keys_and_doors[c] = complex(i,j)
                m[complex(i,j)] = c
            else:
                m[complex(i,j)] = c

    moves = [complex(1,0), complex(-1,0), complex(0,1), complex(0,-1)]
    pos = start

    G = nx.Graph()
    #data = np.array([np.array([k.real, k.imag]) for k,v in m.items() if v != '#' and not v.isupper()])
    data = np.array([np.array([k.real, k.imag]) for k,v in m.items() if v != '#'])
    tree = cKDTree(data) 

    for i,j in tree.query_pairs(r=1):
        G.add_edge(complex(data[i,0], data[i,1]), complex(data[j,0], data[j,1]))

    G2 = nx.DiGraph()
    keys = [k for k in keys_and_doors.keys() if k.islower()]
    for k1, k2 in itertools.permutations(keys, 2):
        try:
            path = find_path(k1, k2)
            for c1, c2, l in path:
                G2.add_edge(c1, c2, weight=l)
        except ValueError:
            continue
    for k in keys:
        try:
            path = find_path('@', k)
            for c1, c2, l in path:
                G2.add_edge(c1, c2, weight=l)
        except ValueError:
            continue

    plt.subplot(111)
    nx.draw(G2, with_labels=True)
    plt.show()


    # J = dict()
    # node = 's'
    # total_length = 0
    # remaining_keys = keys.keys()
    # stacks = defaultdict(set)
    # stacks[node] = set(k for k,v in keys.items() if nx.has_path(G, pos, v))
    # import pdb; pdb.set_trace()
    # while stacks:
        # if not stacks[node]:
            # print('reached bottom')
            # J[node] = 0
            # node = node[:-1]
            # continue

        # k = stacks[node].pop()
        # prev = node
        # node += k
        # l = nx.shortest_path_length(G, pos, keys[k])

        # if node in J.keys():
            # costs[prev][node] =  l + J[node]
            # continue

        # pos = keys[k]
        # remaining_keys -= set(k)

        # print('collecting', k, 'has left', remaining_keys)
        # if k in doors.keys():
            # print('unlocking', k.upper())
            # door = doors[k]
            # for i in tree.query_ball_point([door.real, door.imag], 1):
                # G.add_edge(door, complex(data[i,0], data[i,1]))
        # stacks[node] = set(k for k in remaining_keys if nx.has_path(G, pos, keys[k]))

    # print(d)
