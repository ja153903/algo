from data_structures.tree import TreeNode

from typing import Optional


# This problem should scream postorder traversal
# since we want to work with the values with a
# bottom-up approach
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        """
        if root is None, then we know we're done
        if we have a node that has no children, then this is a leaf, must remove if value is equal to target
        else we recurse down further
        """
        if not root:
            return None

        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)

        root.left = left
        root.right = right

        if not left and not right:
            if root.val == target:
                return None

        return root
