import pytest
from day2.day2 import is_game_possible
from day2.day2 import is_red_possible, is_green_possible, is_blue_possible
from day2.day2 import get_game_power

games = [
    'Game 1: 1 green, 1 blue, 1 red; 3 green, 1 blue, 1 red; 4 green, 3 blue, 1 red; 4 green, 2 blue, 1 red; 3 blue, 3 green',
    'Game 88: 2 green, 2 red, 4 blue; 4 blue, 4 green, 12 red; 2 green, 3 blue, 4 red; 2 green, 2 blue, 12 red; 4 blue, 8 red, 2 green',
    'Game 25: 16 red, 8 green; 2 red, 3 blue; 10 green, 5 red, 4 blue; 9 red, 7 green; 7 red, 6 blue',
    'Game 33: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

def test_game0():
    assert is_game_possible(games[0]) == (True, 1)

def test_game88():
    assert is_game_possible(games[1]) == (True, 88)

def test_game25():
    assert is_red_possible(games[2])[0] == False

def test_powergame3():
    assert get_game_power(games[3]) == 48

def test_powergame33():    
    assert get_game_power(games[4]) == 12
    assert get_game_power(games[5]) == 1560
    assert get_game_power(games[6]) == 630
    assert get_game_power(games[7]) == 36

def test_minredgame33():
    assert is_red_possible(games[3])[1] == 4
    assert is_green_possible(games[3])[1] == 2
    assert is_blue_possible(games[3])[1] == 6