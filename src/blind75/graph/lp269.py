"""
There is a new alien language that uses the English alphabet.
However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's
dictionary, where the strings in words are sorted lexicographically
by the rules of this new language.

Return a string of the unique letters in the new alien language 
sorted in lexicographically increasing order by the new language's rules.
If there is no solution, return "'. If there are multiple solutions,
return any of them.

--------
Approach
--------
This is a topological sort problem. The toughest part here is understanding
how the question works.
"""
from typing import List
from collections import defaultdict, Counter, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: create data structures + the indegree of each unique letter to 0.
        adj_list = defaultdict(set)
        indegree = Counter({c: 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and indegree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegree[d] += 1
                    break
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in indegree if indegree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(indegree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
