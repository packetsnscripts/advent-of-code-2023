import os
from typing import List

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__name__))
INPUT_FILES_DIR = f"{PROJECT_ROOT_DIR}/puzzle_input/"

SPELLED_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

#Read input file and return a list of strings
def read_input_file(day_num: int) -> List[str]:
    day_n_file = f"{INPUT_FILES_DIR}day{day_num}"
    with open(day_n_file) as f:
        data = f.read()
    return data.splitlines()

def get_number_from_string(input_line:str) -> int:
    first_digit: int
    last_digit: int
    #key = position in string, value = number
    number_position_dict = {}
    for num in SPELLED_NUMBERS.keys():
        if num in input_line:
            number_position_dict[input_line.find(num)] = num
    for char in input_line:
       if char.isdigit():
           number_position_dict[input_line.find(char)] = char

    number_position_ordered = sorted(number_position_dict)

    #Extracting first digit
    if(number_position_dict[number_position_ordered[0]] in SPELLED_NUMBERS.keys()):
        first_digit = SPELLED_NUMBERS[number_position_dict[number_position_ordered[0]]]
    else:
        first_digit = int(number_position_dict[number_position_ordered[0]])
    #Extracting last digit
    if(number_position_dict[number_position_ordered[-1]] in SPELLED_NUMBERS.keys()):
        last_digit = SPELLED_NUMBERS[number_position_dict[number_position_ordered[-1]]]
    else:
        last_digit = int(number_position_dict[number_position_ordered[-1]])   

    return (first_digit*10 + last_digit)


def get_sum_of_list(numlist:list) -> int:
    sum = 0
    for num in numlist:
        sum+=num
    return sum

def main():
    numbers = []
    input_strings = read_input_file(1)
    for string in input_strings:
        string = string.strip()
        number = get_number_from_string(string)
        numbers.append(number)
    print(get_sum_of_list(numbers))

main()
