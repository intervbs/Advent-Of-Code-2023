import time
import re

numbers = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

if __name__ == '__main__':
    start = time.perf_counter()
    total = 0
    with open('day1.txt', 'r') as input:
        for line in input:
            pattern = re.compile(r'(?:' + '|'.join(re.escape(word) for word in numbers.keys()) + r')')
            string = pattern.sub(lambda match: ''.join(char for char in numbers[match.group(0)] if char.isdigit()), line)
            string = re.sub(r'\D', '', string)
            if len(string) > 1:
                total = total + int(f'{string[0]}{string[-1]}')
                #print(len(string))
    print(time.perf_counter()-start)
    print(total)
