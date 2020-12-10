from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import timeit
from functools import cache

def adaptor(data):
    return max(j for j in data) + 3

def p1(G):
    path = nx.dag_longest_path(G)
    diffs = [p_ - p for p, p_ in zip(path, path[1:])]
    return diffs.count(1) * diffs.count(3)

def p2(G, a):
    return sum(1 for _ in nx.all_simple_paths(G, 0, a))

@cache
def N(G, c, a):

    if c == a:
        return 1

    ns = list(nx.neighbors(G, c))

    if len(ns) == 1:
        return N(G, ns[0], a)
    else:
        return sum(N(G, n, a) for n in ns)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        data = [int(j) for j in data]
        a = adaptor(data)
        data.append(a)
        data.sort()

    G = nx.DiGraph()
    s = set({0})

    while s:
        c = s.pop()
        ns = [c+i for i in range(1, 4)]
        e = [(c, n) for n in ns if n in data]
        G.add_edges_from(e)
        s |= set(n for _, n in e)

    print(p1(G))
    print(N(G, 0, a))

    #options = {'node_color': 'black',
    #        'node_size': 100,
    #        'width': 1}
    #nx.draw(G, **options)
    #plt.show()
