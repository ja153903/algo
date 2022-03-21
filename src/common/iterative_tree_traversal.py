"""
When solving questions like finding the kth Smallest of a binary search tree,
we can use the iterative method for tree traversal

Other Applications
------------------
* Validating if BST is in order
"""
from typing import Optional

from data_structures.tree import TreeNode


def get_kth_smallest(root: Optional[TreeNode], k: int) -> int:
    if not root:
        return -1

    stack = []

    while root or stack:
        # go through all left elements
        while root:
            stack.append(root)
            root = root.left

        # evaluate the elements
        root = stack.pop()
        k -= 1

        if k == 0:
            return root.val

        # go to elements on right
        root = root.right

    return -1
