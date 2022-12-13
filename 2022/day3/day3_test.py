import sys
from day3 import calc_priority_rucksack

with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
print(calc_priority_rucksack(test_input))