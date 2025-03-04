from typing import List
import pytest


def count_complete_day_pairs(hours: List[int]) -> int:
    counter = 0
    for i in range(len(hours)):
        for j in range(i+1, len(hours)):
            if (hours[i] + hours[j]) % 24 == 0:
                counter += 1
    return counter


@pytest.mark.parametrize("input_list, expected_output", [
    ([12, 12, 30, 24, 24], 2),
    ([72, 48, 24, 3], 3)
])


def test_reverse_list(input_list, expected_output):
    hours = input_list
    assert count_complete_day_pairs(hours) == expected_output