import sys
from day6 import contain_duplicate, slicing_packet, slicing_packet_2

with open('input_test.txt') as f:
    line = f.readlines()
    test_input = ''.join(line)
    
print(contain_duplicate(test_input))
print(slicing_packet_2(test_input, 14))
#slicing_packet('abcbaz')