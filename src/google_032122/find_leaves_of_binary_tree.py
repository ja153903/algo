from data_structures.tree import TreeNode
from typing import Optional, List


"""
---------------
Time Complexity
---------------

This code takes O(n) time since we'll need to
iterate over all nodes in the list
"""
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # since this problem requires us to work from the bottom up,
        # this means that we should use some sort of post-order traversal
        # we should also keep track of the height of each node, because
        # we need to group the nodes together.
        result = []

        def postorder(root: Optional[TreeNode]) -> int:
            if not root:
                return -1

            left = postorder(root.left)
            right = postorder(root.right)

            height = 1 + max(left, right)

            nonlocal result
            if len(result) == height:
                result.append([])

            result[height].append(root.val)

            return height

        postorder(root)

        return result
