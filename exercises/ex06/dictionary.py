"""Exercise 06 - Dictionaries."""

__author__ = "730506302"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values for a dictionary."""
    result: dict[str, str] = {}
    for key1 in input:
        key2 = input[key1]
        result[key2] = key1
    if len(input) != len(result):
        raise KeyError
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary with unique elements from a list and the number of times they appear."""
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] = result[item] + 1
        else:
            result[item] = 1
    return result


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns a dictionary with unique elements from a list and the number of times they appear."""
    result: str = ""
    highest: int  = -1
    for key1 in input_dict:
        counter: int = 0
        for key2 in input_dict:
            if input_dict[key1] == input_dict[key2]:
                counter += 1
        if highest < counter:
            highest = counter
            result = input_dict[key1]
    return result