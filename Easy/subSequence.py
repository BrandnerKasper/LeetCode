from typing import List

import pytest


def max_sub_sequence(nums: List[int], k: int) -> List[int]:
    l = sorted(nums, reverse=True)
    l = l[0:k]
    remove = l[-1]
    result = [x for x in nums if x>= remove]
    while len(result) > k:
        result.reverse()
        result.remove(min(result))
        result.reverse()
    return result


@pytest.mark.parametrize("input_elements, expected", [
    ([[3,4,3,3], 2], [3,4]),
    ([[-16,-13,8,16,35,-17,30,-8,34,-2,-29,-35,15,13,-30,-34,6,15,28,-23,34,28,-24,15,-17,10,31,32,-3,-36,19,31,-5,-21,-33,-18,-23,-37,-15,12,-28,-40,1,38,38,-38,33,-35,-28,-40,4,-15,-29,-33,-18,-9,-29,20,1,36,-8,23,-34,16,-7,13,39,38,7,-7,-10,30,9,26,27,-37,-18,-25,14,-36,23,28,-15,35,-9,1], 8], [35,34,38,38,36,39,38,35]),
    ([[2,1,3,3], 2], [3,3]),
    ([[-1,-2,3,4], 3], [-1,3,4]),
    ([[50,-75], 2], [50, -75])
])


def test_reverse_list(input_elements, expected):
    nums = input_elements[0]
    k = input_elements[1]
    assert max_sub_sequence(nums, k) == expected