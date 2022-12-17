import sys
from day4 import camp_cleanup

with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
print(camp_cleanup(test_input))    