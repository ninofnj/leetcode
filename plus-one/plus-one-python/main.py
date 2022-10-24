from typing import List

import pytest


def plus_one(digits: List[int]):
    n = len(digits)
    carry = 1
    for i in range(n):
        if carry == 1:
            digits[n - i-1] += 1
        if digits[n - i-1] > 9:
            digits[n - i-1] = 0
            carry = 1
        else:
            carry = 0
    if carry == 1:
        digits = [1] + digits
    return digits


test_data = [
    ([9], [1, 0]),
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
]


@pytest.mark.parametrize("digits, expected", test_data)
def test_plus_one(digits, expected):
    print("digits")
    print(digits)
    assert plus_one(digits) == expected
