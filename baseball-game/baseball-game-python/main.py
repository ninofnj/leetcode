from typing import List

import pytest


def add_score(scores: List[int], score: str) -> List[int]:
    return scores + [int(score)]


def sum_last_two_scores(scores: List[int]) -> List[int]:
    return scores + [scores[-1] + scores[-2]]


def duplicate_last_score(scores: List[int]) -> List[int]:
    return scores + [scores[-1] * 2]


def invalidate_last_score(scores: List[int]) -> List[int]:
    return scores[:-1]


def sum_scores(scores: List[int]) -> int:
    total = 0
    for score in scores:
        total += score
    return total


def calc_points(ops: List[str]) -> int:
    scores = list()
    operation_types = {
        "+": sum_last_two_scores,
        "D": duplicate_last_score,
        "C": invalidate_last_score,
    }
    for operation in ops:
        if operation in operation_types:
            scores = operation_types[operation](scores)
        else:
            scores = add_score(scores, operation)

    return sum_scores(scores)


test_data = [
    (["5", "2", "C", "D", "+"], 30),
    (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
    (["1"], 1),
]


@pytest.mark.parametrize("ops, expected", test_data)
def test_calc_points(ops, expected):
    assert calc_points(ops) == expected


def test_add_score():
    assert add_score([5], "2") == [5, 2]


def test_sum_last_scores():
    assert sum_last_two_scores([5, 10]) == [5, 10, 15]


def test_duplicate_last_score():
    assert duplicate_last_score([5]) == [5, 10]


def test_invalidate_last_score():
    assert invalidate_last_score([5, 2]) == [5]


def test_sum_scores():
    assert sum_scores([5, 10, 15]) == 30
