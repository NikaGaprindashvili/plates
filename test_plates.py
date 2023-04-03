import pytest
from plates import is_valid

def test_valid_plate():
    assert is_valid("AB1234") == True

def test_too_short_plate():
    assert is_valid("A") == False

def test_too_long_plate():
    assert is_valid("ABC12345") == False

def test_non_alpha_start():
    assert is_valid("123ABC") == False

def test_non_alpha_second():
    assert is_valid("A1BCDE") == False

def test_zero_first():
    assert is_valid("0A1234") == False

def test_middle_number():
    assert is_valid("ABC1D2") == False

def test_invalid_characters():
    assert is_valid("AB C!23") == False
