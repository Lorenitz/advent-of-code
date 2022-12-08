import sys
from day2 import get_final_results


with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
print(get_final_results(test_input))
