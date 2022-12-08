def find_max_calories (input):
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
        
    return max(calorie_per_elf)

if __name__ == '__main__':
       
    with open('input.txt') as f:
        lines = f.readlines()
        test_input = ''.join(lines)
        
    print(find_max_calories(test_input))