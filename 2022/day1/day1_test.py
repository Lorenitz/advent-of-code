import sys
from day1 import find_top_one_calorie, find_top_three_calories



with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
print(find_top_one_calorie(test_input))

print(find_top_three_calories(test_input))
