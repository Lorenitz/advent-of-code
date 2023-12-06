
num_dict = {
    "one": 1, 
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1, 
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
    }

def convert_line_to_numbers(line):
    slice_start = 0
    line_result = []
    
    for i in range(len(line)+1):
        slice_to_analyze = line[i:]
        
        # Replace written numbers with numerical values
        for word, number in num_dict.items():
            if slice_to_analyze.startswith(word):
                line_result.append(number)
                # slice_start = i
                
    return line_result    
 

def calibration_part_1(input):
    
    
    calibration_value = input.split("\n")
   # print(input)
   # print(calibration_value)
    

    numbers_list = []
    for item in calibration_value:
        numbers_list.append(convert_line_to_numbers(item))
    #     print(convert_line_to_numbers(item))
    #     numbers = []
    #     for char in item:
    #         if char.isdigit():
    #             numbers.append(int(char))
    #     numbers_list.append(numbers)
 

    final_list = []

    for item in numbers_list:
        first_value = None
        second_value = None

        for value in item:
        
            if first_value == None:
                first_value = item[0]
            second_value = value
        
        final_list.append(int(str(first_value) + str(second_value)))
        
    return sum(final_list)
    
    
    


if __name__ == '__main__':
       
    with open('input.txt') as f:
        lines = f.readlines()
        test_input = ''.join(lines)

#print(convert_line_to_numbers(test_input))
print(calibration_part_1(test_input))
