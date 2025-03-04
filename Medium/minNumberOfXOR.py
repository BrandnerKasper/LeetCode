from typing import List
import pytest


def min_operations(nums: List[int], k: int) -> int:
    n = 0
    for num in nums:
        n ^= num
    n = bin(n)
    k = bin(k)
    if len(n) > len(k):
        k = '0b' + k[2:].zfill(len(n)-2)
    else:
        n = '0b' + n[2:].zfill(len(k)-2)
    return  sum(bit_k != bit_result for bit_k, bit_result in zip(k, n))


@pytest.mark.parametrize("input_list, expected_output", [
    ([[3,13,9,8,5,18,11,10], 13], 2),
    ([[2, 1, 3, 4], 1], 2),
    ([[2, 0, 2, 0], 0], 0)
])


def test_reverse_list(input_list, expected_output):
    nums = input_list[0]
    k = input_list[1]
    assert min_operations(nums, k) == expected_output