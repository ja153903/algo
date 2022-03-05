class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


"""
=== Solution ===
We need to keep track of our copies within some dictionary
at the same time we should be iterating over the entire graph
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        copies = {}
        clone = Node(node.val)

        copies[node] = clone

        queue = deque()
        queue.append(node)

        while queue:
            front = queue.popleft()

            for child in front.neighbors:
                if child not in copies:
                    copies[child] = Node(child.val)
                    queue.append(child)

                copies[front].neighbors.append(copies[child])

        return clone
