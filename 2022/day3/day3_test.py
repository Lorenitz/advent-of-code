import sys
from day3 import calc_priority_rucksack
from day3 import rucksack_reorganization

with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
#print(calc_priority_rucksack(test_input))
print(rucksack_reorganization(test_input))