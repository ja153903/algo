from data_structures.tree import TreeNode
from typing import Optional, List


"""
We have to keep track of paths around left and right

We have to start from the root and find the start value
We have to start from the root and also find the dest value

Once we've constructed the path, we want to make sure that
we remove items from the path that are common
"""


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def find(node: Optional[TreeNode], value: int, path: List[str]) -> bool:
            if node.val == value:
                return True
            elif node.left and find(node.left, value, path):
                path += "L"
            elif node.right and find(node.right, value, path):
                path += "R"

            return path

        left_path, right_path = [], []
        find(root, startValue, left_path)
        find(root, destValue, right_path)

        # remove nodes that are the same
        while left_path and right_path and left_path[-1] == right_path[-1]:
            left_path.pop()
            right_path.pop()

        return "".join(["U" for _ in range(len(left_path))]) + "".join(
            reversed(right_path)
        )
