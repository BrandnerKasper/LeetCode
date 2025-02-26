import pytest


# Single Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


# Helper functions
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


@pytest.mark.parametrize("input_list, expected_output", [
    ([], []),
    ([1, 2], [2, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([42], [42])
])


def test_reverse_list(input_list, expected_output):
    head = list_to_linkedlist(input_list)
    reversed_head = reverseList(head)
    output_list = linkedlist_to_list(reversed_head)
    assert output_list == expected_output





