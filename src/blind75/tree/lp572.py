from data_structures.tree import TreeNode

from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not root and not sub_root:
            return True

        if not root or not sub_root:
            return False

        result = False

        if root.val == sub_root.val:
            result = self.is_same_tree(root, sub_root)

        return (
            result
            or self.isSubtree(root.left, sub_root)
            or self.isSubtree(root.right, sub_root)
        )

    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (
            p.val == q.val
            and self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right)
        )
