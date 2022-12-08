import sys
from day1 import find_max_calories



with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
print(find_max_calories(test_input))