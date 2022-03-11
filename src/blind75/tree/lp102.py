from typing import List, Optional
from data_structures.tree import TreeNode

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)

            subresult = []

            for _ in range(size):
                front = queue.popleft()
                subresult.append(front.val)

                if front.left:
                    queue.append(front.left)

                if front.right:
                    queue.append(front.right)

            result.append(subresult)

        return result
