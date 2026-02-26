import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("буква", "Буква"),
    ("буква это часть слова", "Буква это часть слова"),
    ("Буква", "Буква"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize("input_str, expected", [
    ("123смк", "123смк"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


    #2


@pytest.mark.parametrize("input_str, expected", [
    ("   3 пробела", "3 пробела"),
    ("Нет пробела", "Нет пробела"),
    ("", ""),
])
def test_trim_positive (input_str, expected):
    whitespace = " "
    while input_str.startswith(whitespace):
        input_str = input_str.removeprefix(whitespace)
    assert string_utils.trim(input_str) == expected


# Негативный тест

@pytest.mark.parametrize("input_str, expected", [
    ("3 пробела в конце   ", "3 пробела в конце   "),
    ("      ", ""),
    ("", ""),
])
def test_trim_negative (input_str, expected):
    whitespace = " "
    while input_str.startswith(whitespace):
        input_str = input_str.removeprefix(whitespace)
    assert string_utils.trim(input_str) == expected


    #3

@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("Символ", "С", True),
    ("Символ", "R", False),
    (".", ".", True),
])
def test_contains_positive(input_str, symbol_str, expected):
    assert string_utils.contains(input_str, symbol_str) == expected

@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("Символ #", "#", True),
    ("Символ", "В", False),
    (" ", " ", True),
])
def test_contains_negative(input_str, symbol_str, expected):
    assert string_utils.contains(input_str, symbol_str) == expected



    #4

@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("удаление", "удаление", ""),
    ("удаление", "е", "удални"),
])
def test_delete_symbol_positive(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected


@pytest.mark.parametrize("input_str, symbol_str, expected", [
    ("123", "a", "123"),
    ("   ", " ", ""),
])
def test_delete_symbol_negative(input_str, symbol_str, expected):
    assert string_utils.delete_symbol(input_str, symbol_str) == expected






