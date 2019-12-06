import networkx as nx
from collections import defaultdict

def get_orbits(lines):
    g = defaultdict(list)
    for line in lines:
        center, orbiter = line.split(')')[0:2]
        g[orbiter].append(center)
    return g

def get_orbit_graph(lines):
    G = nx.Graph()
    for line in lines:
        center, orbiter = line.split(')')[0:2]
        G.add_edge(orbiter, center)
    return G

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        g = get_orbit_graph(lines)
        print(sum(v for v in nx.single_source_shortest_path_length(g, 'COM').values()))

        start = g.neighbors('YOU').next()
        end = g.neighbors('SAN').next()
        print(nx.shortest_path_length(g, start, end))

