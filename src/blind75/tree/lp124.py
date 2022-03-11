from typing import Optional
from data_structures.tree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def get_max_gain(node: Optional[TreeNode]) -> int:
            nonlocal max_path
            if not node:
                return 0

            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)

            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return node.val + max(gain_on_left, gain_on_right)

        get_max_gain(root)

        return max_path

