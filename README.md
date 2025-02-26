# LeetCode
Just a repo to store some solutions for leetcode exercises.

## Example: Add Binary

```python
import pytest

def add_binary(a: str, b: str) -> str:
    list_a = [*a]
    list_b = [*b]
    list_a.reverse()
    list_b.reverse()
    # check which list is shorter/longer
    if len(list_a) <= len(list_b):
        s = list_a
        l = list_b
    else:
        s = list_b
        l = list_a
    for i in range(len(s)):
        if s[i] == "0":
            continue
        if s[i] == "1" and l[i] == "0":
            l[i] = "1"
        elif s[i] == "1" and l[i] == "1":
            flip_bit = False
            for j in range(i, len(l)):
                if l[j] == "0":
                    l[j] = "1"
                    flip_bit = True
                    break
                if l[j] == "1":
                    l[j] = "0"
            if not flip_bit:
                l.append("1")
    l.reverse()
    return "".join(l)


@pytest.mark.parametrize("input_list, expected_output", [
    (["11", "1"], "100"),
    (["1010", "1011"], "10101")
])


def test_reverse_list(input_list, expected_output):
    a = input_list[0]
    b = input_list[1]
    assert add_binary(a, b) == expected_output
```

We utilize the ```pytest``` library to test the provided cases.