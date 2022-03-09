"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

=== Solution ===

If this is supposed to be tackled with a graph approach,
then this feels like a union find problem,
where we look for the largest connected component.

Note that we'll consider something a connected component if it's
within 1 of any element within the connected component
"""
from typing import List
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(i):
            if i != parent[i]:
                parent[i] = parent[parent[i]]
            return parent[i]

        def union(i, j):
            pi, pj = find(i), find(j)
            if pi != pj:
                if rank[pi] >= rank[pj]:
                    parent[pj] = pi
                    rank[pi] += 1
                else:
                    parent[pi] = pj
                    rank[pj] += 1

        if not nums:
            return 0

        parent, rank, nums = {}, {}, set(nums)

        for num in nums:
            parent[num] = num
            rank[num] = 0

        for num in nums:
            if (num - 1) in nums:
                union(num - 1, num)

            if (num + 1) in nums:
                union(num + 1, num)

        d = defaultdict(list)
        for num in nums:
            d[find(num)].append(num)

        return max([len(l) for l in d.values()])
