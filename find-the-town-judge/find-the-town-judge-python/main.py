from typing import List, Tuple

import pytest


def find_town_judge(n: int, trust: List[Tuple[int, int]]):
    person_has_trust = dict()
    person_trust = dict()

    judge = -1

    for person, trust_in in trust:
        if trust_in not in person_has_trust:
            person_has_trust[trust_in] = dict()
        person_has_trust[trust_in][person] = 1

        person_trust[person] = True

    # Find a person who has the trust of all people
    for person in person_has_trust.keys():
        if len(person_has_trust[person].keys()) == n - 1:
            judge = person
            break
    else:
        if n == 1:
            judge = 1

    # Check judge doesn't exists in person_trust
    if judge not in person_trust:
        return judge
    else:
        return -1


test_data = [
    (1, [], 1),
    (2, [(1, 2)], 2),
    (3, [[1, 3], [2, 3]], 3),
    (3, [[1, 3], [2, 3], [3, 1]], -1),
]


@pytest.mark.parametrize("n, trust, expected", test_data)
def test_town_judge(n, trust, expected):
    assert find_town_judge(n, trust) == expected
