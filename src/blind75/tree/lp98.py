from data_structures.tree import TreeNode

from typing import Optional


"""
One strat we can use here is to do an inorder traversal and check if
the BST is sorted
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []

        def inorder(node: Optional[TreeNode]) -> None:
            if node:
                nonlocal result

                inorder(node.left)
                result.append(node.val)
                inorder(node.right)

        inorder(root)

        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                return False

        return True

    def iterative_solution(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if prev and root.val <= prev.val:
                return False
            prev = root

            root = root.right

        return True
