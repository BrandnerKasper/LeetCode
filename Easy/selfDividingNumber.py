from typing import List
import pytest


def self_dividing_numbers(left: int, right: int) -> List[int]:
    l = []
    for i in range(left, right+1):
        nums = [*str(i)]
        append = True
        for num in nums:
            num = int(num)
            if num == 0:
                append = False
                break
            if not i % num == 0:
                append = False
        if append:
            l.append(i)
    return l


@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 22], [1,2,3,4,5,6,7,8,9,11,12,15,22]),
    ([47, 85], [48,55,66,77])
])


def test_reverse_list(input_list, expected_output):
    left = input_list[0]
    right = input_list[1]
    assert self_dividing_numbers(left, right) == expected_output