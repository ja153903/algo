"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

* Collect all the leaf nodes.
* Remove all the leaf nodes.
* Repeat until the tree is empty.

=== Solution ===

The solution to this problem depends on us collecting the item based on height.

The height of a tree by definition is the number of edges from the current node
to the bottom.
"""
from typing import Optional, List

from data_structures.tree import TreeNode


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        self.height(root, result)

        return result
       
    def height(self, root: Optional[TreeNode], result: List[List[int]]) -> int:
        if not root:
            return -1

        level = 1 + max(self.height(root.left, result), self.height(root.right, result))

        # whenever we hit a new level, we add an empty list to the result
        if level == len(result):
            result.append([])
        
        result[level].append(root.val)

        return level
