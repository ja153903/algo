from data_structures.tree import TreeNode

from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = preorder.pop(0)
        node = TreeNode(root)

        root_index = -1
        for i, val in enumerate(inorder):
            if val == root:
                root_index = i
                break

        if root_index == -1:
            return node

        node.left = self.buildTree(preorder, inorder[:root_index])
        node.right = self.buildTree(preorder, inorder[root_index + 1 :])

        return node
