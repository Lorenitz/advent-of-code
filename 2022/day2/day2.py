result_score = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

elf_strategy = {
    "X": "lose",
    "Y": "draw",
    "Z": "win" 
}

elements = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors"
}

element_score = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

def get_final_results(input):
    matches = input.split("\n")
    final_score = 0
    
    for match in matches: 
        # equivalent to:
        #     match_elements = match.split(' ') # ex: ['A','X']
        #     opponent_raw, you_raw = match_elements
        
        #     match_elements = match.split(' ') # ex: ['A','X']
        #     opponent_raw = match_elements[0]
        #     you_raw = match_elements[1]
        opponent_raw, you_raw = match.split(' ')
        
        opponent = elements[opponent_raw]
        you = get_strategy_element(opponent, you_raw)
        print(f"Opponent choose : {opponent}, You choose: {you}, score = {jkpw_match(you, opponent)} ")
        final_score = final_score + jkpw_match(you, opponent)
        
    return final_score

def get_strategy_element(opponent, raw_strategy):
    strategy = elf_strategy[raw_strategy]
    
    if opponent=="rock":
        if strategy=="win":
            return 'paper'
        elif strategy=="lose":
            return 'scissors' 
    if opponent=="paper":
        if strategy=="win":
            return 'scissors'
        elif strategy=='lose':
            return 'rock'
    if opponent=='scissors':
        if strategy=="win":
           return 'rock'
        elif strategy=="lose":
            return 'paper'
        
    return opponent # If draw return the same as the opponent 
            
    

def jkpw_match(you, opponent):
    score = element_score[you]
    result = 'draw'
    
    if you=='rock':
        if opponent=='paper':
            result = 'lose'
        elif opponent=='scissors':
            result = 'win' 
    
    if you =='scissors':
        if opponent =='rock':
            result = 'lose'
        elif opponent =='paper':
            result='win'
    
    if you == 'paper':
        if opponent == 'scissors':
            result='lose'
        elif opponent == 'rock':
            result='win'                        
            
    score = score + result_score[result]
    
    return score

if __name__ == '__main__':
    
    with open('input.txt') as f:
        lines = f.readlines()
        test_input = ''.join(lines)

    print(get_final_results(test_input))
