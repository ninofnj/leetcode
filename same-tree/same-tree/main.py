from typing import Optional, List

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
    # Check if both are None
    if tree1 is None and tree2 is None:
        return True
    # Check if one is None
    elif tree1 is None or tree2 is None:
        return False

    # Check if nodes has same value
    if tree1.val != tree2.val:
        return False

    # Recursive call to validate node
    if not is_same_tree(tree1.left, tree2.left):
        return False
    return is_same_tree(tree1.right, tree2.right)


test_data = [
    (
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(1, TreeNode(2), TreeNode(3)),
        True
    ),
    (
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(1, TreeNode(3), TreeNode(2)),
        False
    ),
    (
        TreeNode(1, TreeNode(3), TreeNode(2)),
        TreeNode(1, TreeNode(2), TreeNode(3)),
        False
    ),
    (
        TreeNode(1, TreeNode(3), TreeNode(2)),
        TreeNode(1, TreeNode(2)),
        False
    ),
    (
        TreeNode(1, TreeNode(3), TreeNode(2)),
        TreeNode(1),
        False
    ),
]


@pytest.mark.parametrize("tree1, tree2, expected", test_data)
def test_same_tree(tree1, tree2, expected: bool):
    assert is_same_tree(tree1, tree2) == expected
