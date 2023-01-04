def follow_instructions(input, stacks):
    #read the instructions to push and pop from test_input
    # for each instruction, we will need to manipulate the steps.
    #instruction_list = input.split("\n")
    command_list = input.split("\n\n") #todo: change with a single \n
    
    for content in command_list:
        each_item = content.split()
        final_command = each_item
        # todo:
        # qty_move = each_item[1]
        # origin = each_item[3]
        # destiny = each_item[5]
           
    list_size = len(final_command)
    final_numerical_list = []
    for item in range(1, list_size,2):
        numerical_command_list = final_command[item]
        final_numerical_list.append(numerical_command_list)
    
    print(final_numerical_list)
    

    
    for i in final_numerical_list:
        qty_move = final_numerical_list[int(i)]
        origin = final_numerical_list[int(i)+1]  
        destiny = final_numerical_list[int(i)+2]  
                
        print(f"qty move: {qty_move}")
        print(f"origin:  {origin}")
        print(f"destiny: {destiny}") 
        
        i = int(i)
        i += 3     
        
    #print(numerical_command_list)
   
    
    #return stacks

#def push(stacks, target, element):    
#    #push: add, plance an element on top of target stack
    
#def pop(stacks, target):
 #   #Pop = remove and return last element
    
  #  return popped_element

#if __name__ == '__main__':
       
#    with open('input.txt') as f:
#        lines = f.readlines()
#        test_input = ''.join(lines)
            
    #print(follow_instruction(test_input, initial_state))
