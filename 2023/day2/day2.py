cubes_rule_qty = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# game_example = {
#     "game_id": 1,
#     "rounds": [
#         {
#             "blue": 3,
#             "red": 4,
#             "green": 0
#         },
#         {
#             "red": 1,
#             "blue": 0,
#             "green":2
#         },
#         {
#             "red":0,
#             "blue":0,
#             "green":2
#         }
#     ],
# }

def parse_games(lines):
    game_list = []
    for line in lines:
        game_list.append(parse_line(line))    
        
    return game_list

def parse_line(line):
    game_object =  {
        "game_id": None,
        "rounds": [],
    }
    [header, body] = line.split(":")
    game_id = int(header.replace('Game ', ''))
    
    game_object['game_id'] = game_id
    
    rounds_raw = body.split(";")
    rounds = []
    
    for round_raw in rounds_raw:
        cubes_raw = round_raw.split(",")
        
        cubes = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        
        for cube in cubes_raw:
            [qtd, color] = cube.strip().split(" ")
            cubes[color] = int(qtd)
        
        rounds.append(cubes)
        
    game_object['rounds'] = rounds   
            
    return game_object


def sum_possible_games(game_list):
    result = 0    
    return result




if __name__ == '__main__':
    with open("2023\\day2\\test_input.txt") as f:
        lines = f.readlines()
        game_list = parse_games(lines)
        print(sum_possible_games(game_list))