#!/usr/bin/env python3

numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def part_one(file):
    total = 0
    with open(file, 'r') as input:
        for line in input:
            first = ''
            for letter in line:
                if letter.isdigit() == True:
                    first = f'{first}{letter}'
            total += int(f'{first[0]}{first[-1]}')
    print(f'Total only numbers: {total}')

def part_two(file):
    total = []
    with open(file, 'r') as input:
        for line in input:
            digit = ''
            for i in range(len(line)):
                if line[i] in ['e', 'f', 'n', 'o', 's', 't']:
                    for pattern_length in range(3, 6):
                        end_index = i + pattern_length
                        pattern = line[i:end_index]

                        if end_index < len(line) and pattern in numbers:
                            digit += numbers[pattern]
                            break

                elif line[i].isdigit():
                    digit += line[i]

            total.append(int(f'{digit[0]}{digit[-1]}'))
    print(f'Correct Total: {sum(total)}')

if __name__ == '__main__':
    file = 'day1.txt'
    part_one(file)
    part_two(file)
