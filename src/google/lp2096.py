from data_structures.tree import TreeNode

from typing import Optional, List


"""
We have root. We have startValue. We have destValue.

From the root, find startValue.
From the root, find destValue.

During this search, we should keep track of the directions we're making
from the root.

For example, if we start from root 5, in search of 3,
Going into left subtree
5 -> 1, 'L'
1 -> 3, 'L'

Going into right subtree in serach of 6
5 -> 2, 'R'
2 -> 6, 'L'

Given these two different paths, we have to combine them somehow.

Note that this is the case, where we found the values in two different
subtrees.

Reverse of L and R is U
"""

# Great job, you had the right idea
class RawSolution:
    def find(self, root: Optional[TreeNode], value: int, path: List[str]) -> bool:
        if not root:
            return False

        if root.val == value:
            return True

        return self.find(root.left, value, path + ["L"]) or self.find(
            root.right, value, path + ["R"]
        )

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        if not root:
            return ""

        if root.val == startValue:
            left_path = []
            right_path = []

            in_left, in_right = self.find(root.left, destValue, left_path), self.find(
                root.right, destValue, right_path
            )

            if in_left:
                return "".join(left_path)

            return "".join(right_path)

        elif root.val == destValue:
            left_path = []
            right_path = []

            in_left, in_right = self.find(root.left, startValue, left_path), self.find(
                root.right, startValue, right_path
            )

            size = max(len(left_path), len(right_path))

            return "".join(["U"] * size)

        left_path = []
        right_path = []

        in_left, in_right = self.find(root.left, startValue, left_path), self.find(
            root.right, destValue, right_path
        )

        if in_left and in_right:
            return self.stitch(left_path, right_path)

        if not in_left and in_right:
            return self.getDirections(root.right, startValue, destValue)

        return self.getDirections(root.left, startValue, destValue)

    def stitch(self, left_path: List[str], right_path: List[str]) -> str:
        # The left path is always going down, so we just need to convert them all to Us
        return "".join(["U"] * len(left_path)) + "".join(right_path)


# The idea with this problem is that we're supposed to take advantage
# of LCA
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, dest: int) -> str:
        def find(node: Optional[TreeNode], value: int, path: List[str]) -> bool:
            if node.val == value:
                return True
            elif node.left and find(node.left, value, path):
                path += "L"
            elif node.right and find(node.right, value, path):
                path += "R"

            return path

        # Note that these paths are accumulated in reverse
        left_path, right_path = [], []
        find(root, start, left_path)
        find(root, dest, right_path)

        # While the ends of these paths are the same, we remove them
        # as we're only concerned about some path from start to dest
        while left_path and right_path and left_path[-1] == right_path[-1]:
            left_path.pop()
            right_path.pop()

        return "".join(["U" for _ in range(len(left_path))]) + "".join(
            reversed(right_path)
        )
