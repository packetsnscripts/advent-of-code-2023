import pytest
from day1.day1 import get_number_from_string

def test_two1nine():
    assert get_number_from_string("two1nine") == 29

def test_eightwothree():
    assert get_number_from_string("eightwothree") == 83

def test_abcone2threexyz():
    assert get_number_from_string("abcone2threexyz") == 13    