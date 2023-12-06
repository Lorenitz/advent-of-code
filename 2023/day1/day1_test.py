import sys
from day1 import calibration_part_1



with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
print(calibration_part_1(test_input))