"""Unit Testing exercise."""

__author__ = "730506302"


def only_evens(given: list[int]) -> list[int]:
    """Function that returns even values from a list."""
    result: list[int] = list()
    i: int = 0
    while i < len(given):
        if given[i] % 2 == 0:
            result.append(given[i])
        i += 1

    return result


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Function that returns a subset of values from given list."""
    result: list[int] = list()
    if a < 0:
        i: int = 0
    else:
        i = a
    if b > len(a_list):
        b = len(a_list)
    while i < b:
        result.append(a_list[i])
        i += 1
    return result


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Function that returns a combined list."""
    result: list[int] = list()
    i: int = 0
    while i < len(list_1):
        result.append(list_1[i])
        i += 1
    j: int = 0
    while j < len(list_2):
        result.append(list_2[j])
        j += 1

    return result