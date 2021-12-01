from collections import OrderedDict
from itertools import groupby
from math import gcd, lcm
import numpy as np
import operator
from functools import reduce

def p1(e, ls):
    t = e
    while True:
        for l in ls:
            if (t % l) == 0:
                return (t - e) * l
        t += 1

def euclidean(a, b):  
    # Base Case  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = euclidean(b%a, a)  
     
    # Update x and y using results of recursive  
    # call  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y 

def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod//n_i # for large p*/
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
        e = int(data[0])
        ls = [int(l) for l in data[1].split(',') if l != 'x']
        #print(p1(e, ls))

        #d = OrderedDict((int(l), -i) for i, l in enumerate(data[1].split(',')) if l != 'x')
        d = dict((int(l), -i) for i, l in enumerate(data[1].split(',')) if l != 'x')
        od = OrderedDict()
        for k in sorted(d.keys()):
            od[k] = d[k]

        print(chinese_remainder(d.keys(), d.values()))
        #it = iter(d.items())

        #l0, a0  = next(it)

        #for l1, a1 in it:
        #    _, m0, m1 = euclidean(l0, l1)
        #    x = a0 * m1 * l1  + a1 * m0 * l0
        #    l0 = l0 * l1
        #    if x < 0:
        #        a0 = x % l0
        #    else:
        #        a0 = x
        #    print(a0)
