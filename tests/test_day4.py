import pytest
from day4.day4 import get_points_for_card

cards = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1'
]

def test_get_points():
    assert get_points_for_card(cards[0]) == 8
    assert get_points_for_card(cards[1]) == 2
    assert get_points_for_card(cards[2]) == 2