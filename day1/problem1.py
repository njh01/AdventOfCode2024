# Advent of code 2024
# day 1
import numpy as np
import pandas as pd

def dataloader(file):
    data = pd.read_csv(file, delimiter='\s+', header=None)
    col1 = sorted(data[0])
    col2 = sorted(data[1])
    return data, col1, col2

def problem1_part1(file):
    data, col1, col2 = dataloader(file)
    total = 0
    for i in range(data.shape[0]):
        diff = np.abs(col2[i] - col1[i])
        total += diff
    print(f"PART ONE - The distance between lists is {total}.")

def problem1_part2(file):
    data, col1, col2 = dataloader(file)
    simularity_score = 0
    for i in range(len(col1)):
        val = col1[i]
        val_count = col2.count(val)
        score = val * val_count
        simularity_score += score
    print(f"PART TWO - The simularity score is {simularity_score}.")

if __name__ == '__main__':
    filein = "input.txt"
    problem1_part1(filein)
    problem1_part2(filein)