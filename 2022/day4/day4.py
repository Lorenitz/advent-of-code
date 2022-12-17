def create_assignment(raw_assignment):
    # Example: raw_assignement = '2-4'
    
    values = raw_assignment.split('-')
    # Result: values = ['2','4']
    assignment = {
        "start": int(values[0]),
        "end": int(values[1])
    }
    
    return assignment
    
    
def check_fully_contains(self, other):    
    
    if (self['start'] >= other['start'] and self['end'] <= other['end']) or (other['start'] >= self['start'] and other['end'] <= self['end']):
        return True
    
    return False

def camp_cleanup(input):
    section_assignments = input.split('\n')
    
    sum_fully_contains = 0
    
    for line in section_assignments:
        elements = line.split(',')
        assign_a = create_assignment(elements[0])
        assign_b = create_assignment(elements[1])       
        result = check_fully_contains(assign_a, assign_b)
        
        sum_fully_contains += int(result)
        
        print(f"{assign_a} fully contains {assign_b} = {result}")
             
   
    return sum_fully_contains



if __name__ == '__main__':
    
    with open('input.txt') as f:
        lines = f.readlines()
        test_input = ''.join(lines)

    print(camp_cleanup(test_input))
