from data_structures.tree import TreeNode

from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if k == 0:
                return root.val

            root = root.right

        return -1
