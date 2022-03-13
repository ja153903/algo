from data_structures.tree import TreeNode

from typing import List, Optional


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, collect a tree's nodes as if you were
        doing this:

        * Collect all the leaf nodes
        * Remove all the leaf nodes
        * Repeat until the tree is empty

        === Solution ===

        Note that all the leaves of a binary tree have a height in common.

        Theoretically, the height of a node is the number of edges from the node
        to leaves.

        So we can group these nodes based on their heights so that we can collect them
        and end up returning this list of lists.
        """
        if not root:
            return []

        result = []

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1

            h = 1 + max(height(node.left), height(node.right))

            nonlocal result
            if h == len(result):
                result.append([])

            result[h].append(node.val)

            return h

        height(root)

        return result
