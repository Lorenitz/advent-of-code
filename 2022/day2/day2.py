result_score = {
    "win": 6,
    "draw": 3,
    "lose": 0
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
        opponent_raw, you_raw = match.split(' ')
        opponent = elements[opponent_raw]
        you = elements[you_raw]
        print(f"Opponent choose : {opponent}, You choose: {you}, score = {jkpw_match(you, opponent)} ")
        final_score = final_score + jkpw_match(you, opponent)
        
    return final_score

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