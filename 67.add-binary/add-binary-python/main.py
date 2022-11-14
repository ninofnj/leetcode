import pytest


def add_binary(a: str, b: str) -> str:
    res = ""
    len_a = len(a) - 1
    len_b = len(b) - 1

    max_len = len_a
    if len_b > max_len:
        max_len = len_b

    i = 0
    carry = 0
    while i <= max_len:
        val_a = int(a[len_a - i]) if i <= len_a else 0
        val_b = int(b[len_b - i]) if i <= len_b else 0
        sum_b = val_a + val_b + carry
        if sum_b > 1:
            carry = 1
            sum_b -= 2
        else:
            carry = 0
        res = str(sum_b) + res
        i += 1
    if carry > 0:
        res = str(carry) + res
    return res


test_data = [
    ("11", "1", "100"),
    ("1010", "1011", "10101"),
    ("1111", "1111", "11110"),
]


@pytest.mark.parametrize("a, b, expected", test_data)
def test_add_binary(a, b, expected):
    assert add_binary(a, b) == expected
