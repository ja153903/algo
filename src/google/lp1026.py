from data_structures.tree import TreeNode
from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0

        def dfs(node: Optional[TreeNode], current: int) -> None:
            nonlocal max_diff

            if not node:
                return

            max_diff = max(max_diff, abs(current - node.val))

            dfs(node.left, current)
            dfs(node.right, current)

        if not root:
            return max_diff

        dfs(root, root.val)
        max_diff = max(self.maxAncestorDiff(root.left), max_diff)
        max_diff = max(self.maxAncestorDiff(root.right), max_diff)

        return max_diff

    def optimal(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.optimal_dfs(root, root.val, root.val)

    def optimal_dfs(self, root: Optional[TreeNode], min_val: int, max_val: int) -> int:
        if not root:
            return max_val - min_val

        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)

        return max(
            self.optimal_dfs(root.left, min_val, max_val),
            self.optimal_dfs(root.right, min_val, max_val),
        )
