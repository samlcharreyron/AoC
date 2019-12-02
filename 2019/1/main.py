import sys
from math import floor

def get_fuel(mass):
    return int(floor(mass / 3) - 2 )

def p1(lines):
    return sum((get_fuel(int(line)) for line in lines))
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    print(p1(lines))

    total_fuel = 0
    for line in lines:
        fuel = get_fuel(int(line))
        while fuel > 0:
            total_fuel += fuel
            fuel = get_fuel(fuel)
    print(total_fuel)
        



