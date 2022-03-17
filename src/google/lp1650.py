class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        path = set()

        current = p

        while current:
            path.add(current)
            current = current.parent

        current = q

        while current:
            if current in path:
                return current

            current = current.parent

        return None
