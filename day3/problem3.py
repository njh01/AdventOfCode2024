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

def problem3_part2(file):
    fopen = open(file,'rb')
    data = str(fopen.read())
    instructions = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)",data)
    if instructions[0] == "do()":
        valid = True
    else: 
        valid = False
    sum = 0
    for entry in instructions:
        if entry == 'do()':
            valid = True
        elif entry == "don't()":
            valid = False
        else:
            if valid:
                numbers = re.findall("\d+",entry)
                product = int(numbers[0]) * int(numbers[1])
                sum += product
    print(f"The sum of valid products in part 2 is {sum}")

if __name__ == '__main__':
    filein = 'input.txt'
    second_file = 'input2.txt'
    problem3_part1(filein)
    problem3_part2(second_file)