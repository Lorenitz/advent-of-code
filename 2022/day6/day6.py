def contain_duplicate(packet):
    
    for pos_a in range(len(packet)):
        for pos_b in range(len(packet)):
            char_a = packet[pos_a]
            char_b = packet[pos_b]
            if pos_a != pos_b and char_a == char_b:
    
             return True
        
        
        
    return False
#Part I
def slicing_packet(packet):
    start = 0
    len_packet = len(packet)
    end = 4
    while end <= len(packet):
        moved_packet = packet[start:end]
        print(moved_packet)
        start +=1
        end +=1  
        if not contain_duplicate(moved_packet):
            return end-1
#Part II     
def slicing_packet_2(packet, size):
    end = size
    len_packet = len(packet)
    for end in range(end, len_packet):
        start = end-size
        moved_packet = packet[start:end]
        print(moved_packet)
        if not contain_duplicate(moved_packet):
            return end
    