"""Testing for Exercise 06."""

__author__ = "730506302"

import pytest
from dictionary import invert, count, favorite_color

with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_none() -> None:
    """Test for Invert function."""
    a_dict: dict[str, str] = {}
    invert(a_dict)


def test_invert_one() -> None:
    """Test for Invert function with one value."""
    a_dict: dict[str, str] = {"a": "a value"}
    invert(a_dict)


def test_invert_multiple() -> None:
    """Test for Invert function with multiple values."""
    a_dict: dict[str, str] = {"a": "a value", "b": "another value"}
    invert(a_dict)


def test_count_none() -> None:
    """Test for Count function with no values in list."""
    a_list: list[str] = []
    count(a_list)


def test_count_one() -> None:
    """Test for Count function with one value in list."""
    a_list: list[str] = ["car"]
    count(a_list)


def test_count_multiple() -> None:
    """Test for Count function with multiple values in list."""
    a_list: list[str] = ["car", "bus", "train", "car"]
    count(a_list)


def test_favorite_color_none() -> None:
    """Test for Favorite Color function with no values."""
    a_dict: dict[str, str] = {}
    favorite_color(a_dict)


def test_favorite_color_diff() -> None:
    """Test for Favorite Color function with different no. of values."""
    a_dict: dict[str, str] = {"a": "blue", "b": "red", "c": "blue", "d": "blue", "e": "red"}
    favorite_color(a_dict)


def test_favorite_color_same() -> None:
    """Test for Favorite Color function with equal no. of values."""
    a_dict: dict[str, str] = {"a": "blue", "b": "red", "c": "blue", "d": "blue", "e": "red", "f": "red"}
    favorite_color(a_dict)