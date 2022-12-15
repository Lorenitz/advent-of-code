ITEM_PRIORITY = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

def calc_priority_rucksack(input):
    rucksack_list = input.split("\n")
    
    priority_sum = 0
    
    for rucksack_content in rucksack_list:
        compartiment_size= int(len(rucksack_content)/2)
        
        rucksack = { 
            "compartment_a":rucksack_content[:compartiment_size],
            "compartment_b":rucksack_content[compartiment_size:],
            "common_item":'',
            "priority":0
        }
        
        
        for item_a in rucksack["compartment_a"]:
            for item_b in rucksack["compartment_b"]:
                if item_a == item_b:
                    rucksack["common_item"] = item_a
                    
        rucksack["priority"]=ITEM_PRIORITY[rucksack["common_item"]]
        
        priority_sum = priority_sum + rucksack["priority"]
        
                 
        print(rucksack)        
                
    return priority_sum
 
def rucksack_reorganization(input):
    rucksack_list = input.split("\n")
    
    priority_sum = 0
    j=3
    for i in range(0,len(rucksack_list),3):
        rucksacs=rucksack_list[i:j]
        j += 3
        
        rucksack = { 
                "common_item":'',
                "priority":0
            }
        
        for item_a in rucksacs[0]:
            for item_b in rucksacs[1]:
                for item_c in rucksacs[2]:
                    if item_a == item_b == item_c:
                        rucksack["common_item"] = item_a
        
        rucksack["priority"]=ITEM_PRIORITY[rucksack["common_item"]]
        
        priority_sum = priority_sum + rucksack["priority"]
        
        #print(rucksacs)
        #print(rucksack)
        
        #print(priority_sum)    
    
    return priority_sum
      
      
if __name__ == '__main__':
    
    with open('input.txt') as f:
        lines = f.readlines()
        test_input = ''.join(lines)

    #print(calc_priority_rucksack(test_input))
    print(rucksack_reorganization(test_input))
