import matplotlib.pyplot as plt
import networkx as nx
import operator
import copy
import sympy as sym

"""
                  root
                    +
        pppw           sjmn
        /                 *
    cczh   lfqf (4)    drzm   dbpl
     +
sllz  lgvd
root = 
"""

op_code_2_op = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def dfs(g, node = 'root'):
    n = g.nodes[node]
    if 'value' in n:
        return n['value']
    else:
        left, right = g.successors(node)
        n['value'] = op_code_2_op[n['op_code']](dfs(g, left), dfs(g, right))
        return n['value']

def part2(g, node):
    if node == 'humn':
        return sym.Symbol('humn')

    n = g.nodes[node]
    if 'value' in n:
        return sym.Integer(n['value'])
    else:
        left, right = g.successors(node)
        if n['op_code'] == '+':
            return sym.Add(part2(g, left), part2(g, right))
        elif n['op_code'] == '-':
            return sym.Add(part2(g, left), sym.Mul(-1, part2(g, right)))
        elif n['op_code'] == '*':
            return sym.Mul(part2(g, left), part2(g, right))
        else:
            return sym.Mul(part2(g, left), sym.Pow(part2(g, right), -1))

if __name__ == '__main__':
    with open('input', 'r') as f:
        lines = f.read().splitlines()

    g = nx.DiGraph()
    for line in lines:
        node = line[:4]
        # check if line[6] is a letter
        if line[6].islower():
            op_code = line[11]
            assert op_code in '+-/*'
            left = line[6:10]
            right = line[13:17]
            g.add_node(node, op_code=op_code, left=left, right=right)
            g.add_edge(node, left)
            g.add_edge(node, right)
        else:
            num = int(line[6:])
            g.add_node(node, value=num)

    print(dfs(copy.deepcopy(g), 'root'))

    left, right = g.successors('root')
    print(sym.solve(part2(g, left) - part2(g, right), 'humn'))
