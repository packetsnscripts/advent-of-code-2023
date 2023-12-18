import os
import re
from typing import List

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__name__))
INPUT_FILES_DIR = f"{PROJECT_ROOT_DIR}/puzzle_input/"
# Read input file
def read_input_file(day_num: int) -> List[str]:
    day_n_file = f"{INPUT_FILES_DIR}day{day_num}"
    with open(day_n_file) as f:
        data = f.read()
    return data.splitlines()

#get points for card
def get_points_for_card (card: str) -> int:
    #points = 2^(n-1)
    left = card.split('|')[0].split(':')[1]
    right = card.split('|')[1]
    pattern = r"\d+"
    winning_numbers = re.findall(pattern=pattern, string=left)
    our_numbers = re.findall(pattern=pattern, string=right)
    matches = 0
    for item in our_numbers:
        if item in winning_numbers:
            matches += 1
    
    if matches == 0:
        return 0
    else:
        return 2**(matches-1)

def get_matches_for_card (card: str) -> int:
    left = card.split('|')[0].split(':')[1]
    right = card.split('|')[1]
    pattern = r"\d+"
    winning_numbers = re.findall(pattern=pattern, string=left)
    our_numbers = re.findall(pattern=pattern, string=right)
    matches = 0
    for item in our_numbers:
        if item in winning_numbers:
            matches += 1
    
    return matches
    

def main() -> None:
    cards = read_input_file(4)
    points = 0
    card_instances = {}  # dict{key: index, value: number of copies}
    total_cards = 0
    for card in cards:
        points += get_points_for_card(card=card)
        
    print(f"points part 1 = {points}")
    
    
    for index, card in enumerate(cards):
        current_card = index + 1
        matches = get_matches_for_card(card=card)
        
        if current_card in card_instances:
            card_instances[current_card] += 1
        else:
            card_instances[current_card] = 1
        
        to_add = card_instances[current_card]
        for card_num in range(current_card + 1, current_card + 1 + matches):
            if card_num > len(cards):
                break
            else:
                    
                if card_num in card_instances:
                    card_instances[card_num] += to_add
                else:
                    card_instances[card_num] = to_add

            
    for value in card_instances.values():
        total_cards += value
                
    print(f"total number of cards part 2 = {total_cards}")
    
main()