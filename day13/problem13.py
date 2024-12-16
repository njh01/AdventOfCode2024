# Advent of Code 2024
# day 13

import numpy as np
import re
from sympy import Matrix

def problem13_part1(file):
    """
    a_press * ax + b_press * bx = tx
    a_press * ay + b_press * by = ty
    """
    with open(file,'r') as f:
        data = f.readlines()
    cost = 0
    i = 0
    while i < len(data):
        ax, ay = re.findall("\d+",data[i])
        i += 1
        bx, by = re.findall("\d+",data[i])
        i += 1
        tx, ty = re.findall("\d+",data[i])
        i += 2
        mat = Matrix([[ax, bx, tx],[ay,by,ty]])
        solution = mat.rref()
        if float(solution[0][0,2])%1 == 0 and float(solution[0][1,2])%1 == 0:
            a_press = solution[0][0,2]
            b_press = solution[0][1,2]
            cost += 3 * a_press + b_press
    print(f"Total cost: {cost}")

if __name__ == '__main__':
    file = "input.txt"
    problem13_part1(file)