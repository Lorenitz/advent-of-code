def find_calorie_per_elf (input):
    elf_content = input.split("\n\n") 
    
    calorie_per_elf = []
    
    for content in elf_content:
        each_item = content.split('\n')
        total_calories = each_item
        
        each_item_int = []
        for item in each_item:
            each_item_int.append(int(item))
        
       
        item_sum = sum(each_item_int)
        calorie_per_elf.append(item_sum)    
        
    return calorie_per_elf

def find_top_one_calorie (input):
    
    return max(find_calorie_per_elf(input))


def find_top_three_calories (input):
    calorie_per_elf = find_calorie_per_elf(input)
    top_three = sorted(calorie_per_elf, reverse=True)[:3]
    
    return sum(top_three)

if __name__ == '__main__':
       
    with open('input.txt') as f:
        lines = f.readlines()
        test_input = ''.join(lines)
            
    print(find_top_one_calorie(test_input))

    print(find_top_three_calories(test_input))
