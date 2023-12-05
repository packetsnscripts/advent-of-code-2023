import re
import os
from typing import List

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__name__))
INPUT_FILES_DIR = f"{PROJECT_ROOT_DIR}/puzzle_input/"

#Read input file and return a list of strings
def read_input_file(day_num: int) -> List[str]:
    day_n_file = f"{INPUT_FILES_DIR}day{day_num}"
    with open(day_n_file) as f:
        data = f.read()
    return data.splitlines()

def get_sum_of_list(numlist:list) -> int:
    sum = 0
    for num in numlist:
        sum+=num
    return sum

# checks if the all the red draws are les than 12
def is_red_possible (game: str) -> (bool, int):
    max_red = 12
    min_red = 0
    pattern = r"\d+\sred"
    reds = re.findall(pattern=pattern, string=game)
    for turn in reds:
        num_reds = int(turn.split(' ')[0])
        if num_reds > min_red:
            min_red = num_reds
    for turn in reds:
        num_reds = int(turn.split(' ')[0])            
        if (num_reds > max_red):
            return False, min_red
    return True, min_red

def is_green_possible (game: str) -> (bool, int):
    max_green = 13
    min_green = 0
    pattern = r"\d+\sgreen"
    greens = re.findall(pattern=pattern, string=game)
    for turn in greens:
        num_greens = int(turn.split(' ')[0])
        if num_greens > min_green:
            min_green = num_greens
    for turn in greens:
        num_greens = int(turn.split(' ')[0])                  
        if (num_greens > max_green):
            return False, min_green
    return True, min_green

def is_blue_possible (game: str) -> (bool, int):
    max_blue = 14
    min_blue = 0
    pattern = r"\d+\sblue"
    blues = re.findall(pattern=pattern, string=game)
    for turn in blues:
        num_blues = int(turn.split(' ')[0])
        if num_blues > min_blue:
            min_blue = num_blues
    for turn in blues:
        num_blues = int(turn.split(' ')[0])            
        if (num_blues > max_blue):
            return False, min_blue
    return True, min_blue

def is_game_possible (game: str) -> (bool, int):
    game_id = int(game.split(':')[0].split(' ')[1])
    all_games_possible = is_red_possible(game)[0] and is_green_possible(game)[0] and is_blue_possible(game)[0]
    if all_games_possible:
        return True, game_id
    else:
        return False, game_id
    
def get_game_power (game: str) -> int:
    #return max_red * max_green * max_blue
    return is_red_possible(game)[1] * is_green_possible(game)[1] * is_blue_possible(game)[1]

def main() -> None:
    possible_games = []
    power_games = []
    input_strings = read_input_file(2)
    for game in input_strings:
        game = game.strip()
        power = get_game_power(game=game)
        power_games.append(power)
        possible, game_id = is_game_possible(game=game)
        if possible:
            possible_games.append(game_id)
            
    print(f"part1:", get_sum_of_list(possible_games))
    print(f"part2:", get_sum_of_list(power_games))
    print(f"power list: ", power_games)
    print(f"length of power_games:", len(power_games))
    return None

main()