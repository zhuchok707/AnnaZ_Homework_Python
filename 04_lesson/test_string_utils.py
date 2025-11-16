import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)

# ------------------- Тесты для функции trim -------------------


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  Skypro", "Skypro"),
    (" Hello", "Hello"),
    ("    Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123123", "123123"),
    ("", ""),
    ("mama", "mama"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)

# ------------------- Тесты для функции contains -------------------


@pytest.mark.positive
@pytest.mark.parametrize("s, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "k", True),
    ("SkyPro", "o", True),
    ("SkyPro", "X", False),
])
def test_contains_positive(s, symbol, expected):
    assert string_utils.contains(s, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("s, symbol, expected", [
    ("SkyPro", "z", False),
    ("SkyPro", " ", False),
])
def test_contains_negative(s, symbol, expected):
    assert string_utils.contains(s, symbol) == expected


def test_contains_empty_string():
    assert not string_utils.contains("", "a")


def test_contains_none_args():
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")
    with pytest.raises(AttributeError):
        string_utils.contains("hello", None)

# ------------------- Тесты для функции delete_symbol -------------------


@pytest.mark.positive
@pytest.mark.parametrize("s, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("abcabc", "b", "acac"),
])
def test_delete_symbol_positive(s, symbol, expected):
    assert string_utils.delete_symbol(s, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("s, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("abc", "", "abc"),
])
def test_delete_symbol_negative(s, symbol, expected):
    assert string_utils.delete_symbol(s, symbol) == expected


def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
    with pytest.raises(AttributeError):
        string_utils.delete_symbol("SkyPro", None)
