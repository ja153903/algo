"""
There are a total of numCourses courses you have to take labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi]
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.,

=== Solution ===

This problem is equivalent to finding a cycle in a directed graph

We solve this via topological sort
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self,numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Modified topological sort can solve this question of finding
        # a cycle within a acyclic directed graph

        graph = defaultdict(list)
        # the number of prerequisites for some course
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            numCourses -= 1

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return numCourses == 0

