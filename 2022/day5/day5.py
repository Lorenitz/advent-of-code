def follow_instructions(input, stacks, movemultiple):
    #read the instructions to push and pop from test_input
    # for each instruction, we will need to manipulate the steps.
    #instruction_list = input.split("\n")
    command_list = input.split("\n") 
 
    
    for content in command_list:
        each_item = content.split()
        final_command = each_item
        qty_move = each_item[1]
        origin = each_item[3]
        destiny = each_item[5]
        
        if movemultiple == False:
            for i in range(int(qty_move)):
                element_popped = pop(stacks,origin)
                push(stacks, destiny,element_popped)
        else:   
            elements_popped = pop_multiples(stacks, origin, int(qty_move))
            push_multiples(stacks, destiny, elements_popped)
        

def push(stacks, target, element):    
    #push: add, place an element on top of target stack
    stacks[target].append(element)
    return
    
def pop(stacks, target):
   #Pop = remove and return last element
   
    popped_element = stacks[target].pop()
    return popped_element


### Part II

# Description: Instead of one by one, all itens at once

def push_multiples(stacks, target, elements):
    stacks[target] = stacks[target] + elements

def pop_multiples(stacks, target, qtd):
    len_stack = len(stacks[target]) - qtd
    #print(len_stack)
    popped_elements = stacks[target][int(len_stack):]
    stacks[target] = stacks[target][:int(len_stack)]
    
    return popped_elements
  
   
   

if __name__ == '__main__':
       
    with open('input.txt') as f:
        lines = f.readlines()
        input = ''.join(lines)
        
    stacks = {
        "1": ['G', 'D', 'V','Z', 'J', 'S', 'B'],
        "2": ['Z', 'S', 'M', 'G', 'V', 'P'],
        "3": ['C', 'L', 'B', 'S', 'W', 'T', 'Q', 'F'],  
        "4": ['H', 'J', 'G', 'W', 'M', 'R', 'V', 'Q'],
        "5": ['C', 'L', 'S', 'N', 'F', 'M', 'D'],
        "6": ['R', 'G', 'C', 'D'],
        "7": ['H', 'G', 'T', 'R', 'J', 'D', 'S', 'Q'],
        "8": ['P','F', 'V'],
        "9": ['D', 'R', 'S', 'T', 'J']                         
    }
            
    follow_instructions(input, stacks, True)
    
    print(stacks)
