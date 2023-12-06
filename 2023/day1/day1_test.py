import sys
from day1 import calibration_part_1, convert_line_to_numbers



with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
print(calibration_part_1(test_input))

#print(convert_line_to_numbers(test_input))