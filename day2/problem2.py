# Advent of Code 2024
# day 2
import numpy as np
import pandas as pd

def problem2_part1(file):
    data = pd.read_csv(file, delimiter='/s+', header=None)
    safe_levels = [1,3]
    safe = 0
    for row in data[0]:
        row_arr = [int(x) for x in row.split()]
        sum_prev = None
        sum = 0
        flag = 0
        for i in range(len(row_arr)-1):
            diff = row_arr[i+1] - row_arr[i]
            if np.abs(diff) < safe_levels[0] or np.abs(diff) > safe_levels[1]:
                flag = -1
                break
            sum += diff
            if i > 0:
                if sum_prev > 0 and sum < sum_prev:
                    flag = -1
                    break 
                if sum_prev < 0 and sum > sum_prev:
                    flag = -1
                    break
            sum_prev = sum
        if flag > -1:
            safe += 1
    print(f"PART ONE - Safe levels: {safe}")
        
def problem2_part2(file):
    return -999

if __name__ == '__main__':
    filein = "input.txt"
    problem2_part1(filein)
    problem2_part2(filein)