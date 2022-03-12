from data_structures.tree import TreeNode

from typing import Optional


"""
Given that this is a binary search tree,
if root.val > p.val and root.val > q.val, then go into right subtree
else go into left subtree
"""


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
