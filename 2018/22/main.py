import sys
import numpy as np
from collections import namedtuple
import networkx as nx

global target, depth, e, g

Node = namedtuple('Node', ['pos', 'tool'])
visited = set()
REGIONS = 'RWN'

def geo_index(x, y):
    if x == 0 and y == 0:
        return 0
    elif x == target[0] and y == target[1]:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return e[x-1, y] * e[x, y-1]

def erosion_level(x, y):
    return (g[x, y] + depth) % 20183

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines() 

    depth = int(lines[0].split(':')[1].strip())
    temp = lines[1].split(':')[1].strip().split(',')
    target = (int(temp[0]), int(temp[1]))
    SIZE = (target[0] + 80, target[1] + 80)

    # depth = 510
    # target = (10, 10)
    # SIZE = (20, 20)

    c = np.zeros(SIZE, np.uint)
    e = c.copy()
    g = c.copy()

    for x in range(SIZE[0]):
        for y in range(SIZE[1]):
            g[x, y] = geo_index(x, y)
            e[x, y] = erosion_level(x, y)
            c[x,y] = e[x, y] % 3

    # problem 1
    print c[target[0], target[1]]
    print(np.sum(c[0:(target[0] + 1), 0:(target[1] + 1)]))

    # problem 2
    G = nx.Graph()
    TOOLS = 'CTN'
    tools = {'R': 'CT', 'W': 'CN', 'N': 'TN'}

    start = Node((0,0), 'T')
    end = Node(target, 'T')

    # first pass to create all the nodes
    for x in range(SIZE[0]):
        for y in range(SIZE[1]):
            region = REGIONS[c[x, y]]
            available_tools = tools[region]
            for tool in available_tools:
                current = Node((x, y), tool)
                G.add_node(current)

    # second pass to create all the edges
    for current in G.nodes:
        region = REGIONS[c[current.pos]]

        # switching tool
        for new_tool in set(tools[region]).difference(current.tool):
            n = Node(current.pos, new_tool)
            G.add_edge(current, n, weight=7)

        # moving
        pps = [(current.pos[0] - 1, current.pos[1]), (current.pos[0] + 1, current.pos[1]),
                (current.pos[0], current.pos[1] - 1), (current.pos[0], current.pos[1] + 1)]
        for pp in pps:
            is_in_map = pp[0] > -1 and pp[1] > -1  and pp[0] < SIZE[0] and pp[1] < SIZE[1]
            if is_in_map:
                region_pp = REGIONS[c[pp[0], pp[1]]]
                if current.tool in tools[region_pp]:
                    n = Node(pp, current.tool)
                    G.add_edge(current, n, weight=1)

    #print(nx.shortest_path_length(G, start, end))
    print(nx.dijkstra_path_length(G, start, end))
    #print(nx.shortest_path(G, start, end))
