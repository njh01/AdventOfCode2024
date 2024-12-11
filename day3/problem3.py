# Advent of Code 2024
# day 3
import re

def problem3_part1(file):
    fopen = open(file,'rb')
    data = str(fopen.read())
    mul_list = re.findall("mul\(\d+,\d+\)",data)
    sum = 0
    for entry in mul_list:
        numbers = re.findall("\d+",entry)
        product = int(numbers[0]) * int(numbers[1])
        sum += product
    print(f"The sum of valid products is {sum}")

if __name__ == '__main__':
    filein = 'input.txt'
    problem3_part1(filein)