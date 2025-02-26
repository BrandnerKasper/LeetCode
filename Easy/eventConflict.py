from typing import List
import pytest


def have_conflict(ev1: List[str], ev2: List[str]) -> bool:
    s1 = convert_time_to_value(ev1[0])
    e1 = convert_time_to_value(ev1[1])

    s2 = convert_time_to_value(ev2[0])
    e2 = convert_time_to_value(ev2[1])

    return s1 <= s2 <= e1 or s1 <= e2 <= e1 or s2 <= s1 <= e1 <= e2


def convert_time_to_value(event: str) -> int:
    h, m = map(int, event.split(":"))
    return h * 60 + m


@pytest.mark.parametrize("input_list, expected_output", [
    ([["01:15", "02:00"], ["02:00", "02:15"]], True),
    ([["01:00","02:00"], ["01:20","03:00"]], True),
    ([["10:00","11:00"], ["14:00","15:00"]], False),
    ([["15:19","17:56"], ["14:11","20:02"]], True)
])


def test_reverse_list(input_list, expected_output):
    event1 = input_list[0]
    event2 = input_list[1]
    assert have_conflict(event1, event2) == expected_output