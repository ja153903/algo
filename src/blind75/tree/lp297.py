from data_structures.tree import TreeNode

from typing import Deque, Optional, List
from collections import deque


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        self.build_string(root, result)

        return "".join(result)

    def build_string(self, node: Optional[TreeNode], result: List[str]) -> None:
        if not node:
            result.append("X")
            result.append(",")
        else:
            # Do a preorder traversal here
            result.append(str(node.val))
            result.append(",")
            self.build_string(node.left, result)
            self.build_string(node.right, result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = deque(data.split(","))
        return self.build_tree(nodes)

    def build_tree(self, nodes: Deque[str]) -> Optional[TreeNode]:
        val = nodes.popleft()

        if val == "X":
            return None

        node = TreeNode(int(val))
        node.left = self.build_tree(nodes)
        node.right = self.build_tree(nodes)

        return node
