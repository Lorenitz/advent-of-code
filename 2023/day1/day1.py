
def calibration_part_1 (input):

    calibration_value = input.split("\n")
    numbers_list = []


    for item in calibration_value:
        numbers = []
        for char in item:
            if char.isdigit():
                numbers.append(int(char))
        numbers_list.append(numbers)
 

    final_list = []

    for item in numbers_list:
        first_value = None
        second_value = None

        for value in item:
        
            if first_value == None:
                first_value = item[0]
            second_value = value
        
        final_list.append(int(str(first_value) + str(second_value)))
        
    print(sum(final_list))


if __name__ == '__main__':
       
    with open('input.txt') as f:
        lines = f.readlines()
        test_input = ''.join(lines)

print(calibration_part_1(test_input))