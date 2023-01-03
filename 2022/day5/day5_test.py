import sys
from day5 import follow_instructions

with open('test_input.txt') as f:
    lines = f.readlines()
    test_input = ''.join(lines)
    
    stacks = {
        "1": ['Z', 'N'],
        "2": ['M', 'C', 'D'],
        "3": ['P']        
    }
    
    follow_instructions(test_input, stacks)
    
    
# In this exercise, we need to learn the concepts for push, pop in stacks    