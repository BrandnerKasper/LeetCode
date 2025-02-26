from typing import Optional

import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_minimum_difference(root: Optional[TreeNode]) -> int:
    dif = float('inf')  # Start with a large difference
    prev = None  # To keep track of the previous node in inorder traversal

    def inorder(node):
        nonlocal dif, prev
        if node is None:
            return

        inorder(node.left)  # Visit left subtree

        if prev is not None:
            dif = min(dif, abs(node.val - prev.val))  # Update the minimum difference

        prev = node  # Update prev to the current node

        inorder(node.right)  # Visit right subtree

    inorder(root)
    return dif


@pytest.mark.parametrize("input_elements, expected", [
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)), 1),
    (TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49))), 1),
    (TreeNode(236, TreeNode(104, None, TreeNode(227)), TreeNode(701, None, TreeNode(911))), 9)
])


def test_min_diff(input_elements, expected):
    tree = input_elements
    assert get_minimum_difference(tree) == expected