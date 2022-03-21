from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        This problem is basically topological sort. So we use Khan's algorithm here
        """
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for recipe, ingredient_list in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient_list)
            for ingredient in ingredient_list:
                graph[ingredient].append(recipe)


        ans = []
        # we keep everything with indegree 0 (i.e. no prereqs) within the deque
        queue = deque(supplies)
        recipes = set(recipes)

        # remember that for khan's algorithm, we start with items with indegree 0
        while queue:
            curr = queue.popleft()
            # if the item we have now with indegree 0 is in recipes, then its something
            # we want so we add it to our result array
            if curr in recipes:
                ans.append(curr)

            for ingredient in graph[curr]:
                indegree[ingredient] -= 1
                if indegree[ingredient] == 0:
                    queue.append(ingredient)

        return ans
