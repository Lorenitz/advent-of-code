def contain_duplicate(packet):
    
    for pos_a in range(len(packet)):
        for pos_b in range(len(packet)):
            char_a = packet[pos_a]
            char_b = packet[pos_b]
            if pos_a != pos_b and char_a == char_b:
                return True
        
        
        
    return False

def slicing_packet(packet):
    
    for group_char in range(3, len(packet)):
        print[packet[3:len(packet)]]
    
    return