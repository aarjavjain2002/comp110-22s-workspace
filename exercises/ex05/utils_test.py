"""Testing for utils."""

__author__ = "730506302"

from utils import only_evens, sub, concat


def test_only_evens_none() -> None:
    """Unit Test function for edge case."""
    test1: list[int] = [3]
    assert len(only_evens(test1)) == 0


def test_only_evens_one() -> None:
    """Unit Test function for use case."""
    test2: list[int] = [456]
    assert len(only_evens(test2)) == 1
    assert only_evens(test2)[0] == 456


def test_only_evens_multiple() -> None:
    """Unit Test function for use case."""
    test3: list[int] = [1, 2, 3, 4, 25, 56]
    assert len(only_evens(test3)) == 3
    assert only_evens(test3)[0] == 2
    assert only_evens(test3)[1] == 4
    assert only_evens(test3)[2] == 56


def test_sub_empty() -> None:
    """Unit Test function for edge case."""
    test1: list[int] = []
    assert len(sub(test1, 2, 5)) == 0


def test_sub_for_b() -> None:
    """Unit Test function for use case."""
    test2: list[int] = [2, 4, 6, 8, 9]
    assert len(sub(test2, 1, 7)) == 4
    assert sub(test2, 1, 7)[0] == 4
    assert sub(test2, 1, 7)[1] == 6
    assert sub(test2, 1, 7)[2] == 8
    assert sub(test2, 1, 7)[3] == 9


def test_sub_for_a() -> None:
    """Unit Test function for use case."""
    test3: list[int] = [2, 4, 6, 8, 9, 13, 12]
    assert len(sub(test3, -3, 6)) == 6
    assert sub(test3, -3, 6)[0] == 2
    assert sub(test3, -3, 6)[1] == 4
    assert sub(test3, -3, 6)[2] == 6
    assert sub(test3, -3, 6)[3] == 8
    assert sub(test3, -3, 6)[4] == 9
    assert sub(test3, -3, 6)[5] == 13


def test_concat_empty() -> None:
    """Unit Test function for edge case."""
    test1_a: list[int] = []
    test1_b: list[int] = []
    assert len(concat(test1_a, test1_b)) == 0


def test_concat_same_len() -> None:
    """Unit Test function for use case."""
    test2_a: list[int] = [1, 2, 3]
    test2_b: list[int] = [4, 5, 6]
    assert len(concat(test2_a, test2_b)) == 6
    assert concat(test2_a, test2_b)[0] == 1
    assert concat(test2_a, test2_b)[1] == 2
    assert concat(test2_a, test2_b)[2] == 3
    assert concat(test2_a, test2_b)[3] == 4
    assert concat(test2_a, test2_b)[4] == 5
    assert concat(test2_a, test2_b)[5] == 6


def test_concat_diff_len() -> None:
    """Unit Test function for use case."""
    test2_a: list[int] = [1, 2, 3]
    test2_b: list[int] = [4, 5, 6, 7]
    assert len(concat(test2_a, test2_b)) == 7
    assert concat(test2_a, test2_b)[0] == 1
    assert concat(test2_a, test2_b)[1] == 2
    assert concat(test2_a, test2_b)[2] == 3
    assert concat(test2_a, test2_b)[3] == 4
    assert concat(test2_a, test2_b)[4] == 5
    assert concat(test2_a, test2_b)[5] == 6
    assert concat(test2_a, test2_b)[6] == 7