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

def get_number_from_string(input_line:str) -> int:
    first_digit: int
    last_digit: int
    for char in input_line:
        if char.isdigit():
            first_digit = char
            break
    for char in input_line[::-1]:
        if char.isdigit():
            last_digit = char
            break
    return int(first_digit+last_digit)

def get_sum_of_list(numlist:list) -> int:
    sum = 0
    for num in numlist:
        sum+=num
    return sum

def main():
    numbers = []
    input_strings = read_input_file(1)
    for string in input_strings:
        number = get_number_from_string(string)
        numbers.append(number)
    print(get_sum_of_list(numbers))
main()