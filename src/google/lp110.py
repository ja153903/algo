from data_structures.tree import TreeNode

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """a binary tree in which the left and right subtrees of every node differ in height by no more than 1 is balanced"""

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True

        left = height(root.left)
        right = height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
