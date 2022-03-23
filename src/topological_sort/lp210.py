from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Similar to the first Course Schedule question, we'll want to use topological sort here

        The difference with this problem is that we want to return the list of items in our result.

        So ideally, we'll have a list of courses that we can finish.

        When do we return an empty list? If there exists a circular dependency.
        """

        # keep track of result in another list
        result = []
        visited = set()

        graph = defaultdict(set)
        indegree = [0] * num_courses

        for u, v in prerequisites:
            indegree[u] += 1
            graph[v].add(u)

        queue = deque([node for node, count in enumerate(indegree) if count == 0])

        while queue:
            front = queue.popleft()
            result.append(front)
            visited.add(front)

            for next_course in graph.get(front, set()):
                if next_course in visited:
                    return []

                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        if sum(indegree) != 0:
            return []

        return result
