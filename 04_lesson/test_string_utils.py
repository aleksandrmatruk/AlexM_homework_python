import pytest
from string_utils import StringUtils


# ==================== capitalize ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
])
def test_capitalize_positive(input_str, expected):
    assert StringUtils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert StringUtils.capitalize(input_str) == expected


# ==================== trim ====================

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("   hello   ", "hello   "),
])
def test_trim_positive(input_str, expected):
    assert StringUtils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert StringUtils.trim(input_str) == expected


# ==================== contains ====================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),
    (" ", " ", True),
])
def test_contains_positive(string, symbol, expected):
    assert StringUtils.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("", "a", False),
    ("SkyPro", "", False),
])
def test_contains_negative(string, symbol, expected):
    assert StringUtils.contains(string, symbol) is expected


# ==================== delete_symbol ====================

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello", "l", "heo"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert StringUtils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),
    ("", "a", ""),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert StringUtils.delete_symbol(string, symbol) == expected
