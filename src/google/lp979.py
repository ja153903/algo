from data_structures.tree import TreeNode

from typing import Optional


"""
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

=== Idea behind problem ===
Thinking about this problem this way helped me: the algorithm traverses the tree bottom up, 
and while traversing the tree upwards as we go we try to maintain the property that the nodes traversed until now have only one coin, 
if a particular coin has excess coins we simply pass the "remaining balance" upwards, 
and suppose a node has no coins then we allot it one coin and pass the "negative balance" upwards(which really means passing coins downwards from excess nodes). 
Think of the positive flows as passing coins from excess nodes to deficient nodes and the the negative flows as positive flows in the "reverse" direction, 
the number of coins would balance out because they are equal to the number of nodes(the "credit" and "debt" cancel out).
"""
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        moves = 0

        self.dfs(root, moves)

        return moves


    def dfs(self, root: Optional[TreeNode], moves: int) -> None:
        if not root:
            return 0

        left = self.dfs(root.left, moves)
        right = self.dfs(root.right, moves)

        moves += abs(left) + abs(right)

        # note that we have root.val - 1
        return (root.val - 1) + left + right
