import pytest

def xor_operation(n: int, start: int) -> int:
    sums = 0
    for i in range(n):
        sums ^= start + 2 * i
    return sums


@pytest.mark.parametrize("input_list, expected_output", [
    ([5, 0], 8),
    ([4, 3], 8)
])


def test_reverse_list(input_list, expected_output):
    n = input_list[0]
    start = input_list[1]
    assert xor_operation(n, start) == expected_output
