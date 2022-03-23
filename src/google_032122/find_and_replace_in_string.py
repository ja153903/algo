from typing import List


"""
You are given a 0-indexed string s that you must perform k replacement operations on. The replacement operations are given as three 0-indexed parallel arrays, indices, sources, and targets, all of length k.

To complete the ith replacement operation:

Check if the substring sources[i] occurs at index indices[i] in the original string s.
If it does not occur, do nothing.
Otherwise if it does occur, replace that substring with targets[i].
For example, if s = "abcd", indices[i] = 0, sources[i] = "ab", and targets[i] = "eee", then the result of this replacement will be "eeecd".

All replacement operations must occur simultaneously, meaning the replacement operations should not affect the indexing of each other. The testcases will be generated such that the replacements will not overlap.

For example, a testcase with s = "abc", indices = [0, 1], and sources = ["ab","bc"] will not be generated because the "ab" and "bc" replacements overlap.
Return the resulting string after performing all replacement operations on s.

A substring is a contiguous sequence of characters in a string.

-------
Example
-------

Input: s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
Output: "eeebffff"

--------
Approach
--------

Create a list to contain our characters post transformation
If the character does not need to be transformed, then we do nothing to it and just add to the list

basically we check on each indices s[indices[i] : indices[i] + len(sources[i])] == sources[i],
if this is true, then we should replace with target.

join the result list to become a string
"""
class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        result = [""] * len(s)
        replaced = [False]* len(s)

        for idx, src, target in zip(indices, sources, targets):
            current = s[idx: idx + len(src)]
            if current == src:
                result[idx] = target
                for i in range(idx, idx + len(src)):
                    replaced[i] = True

        for i, val in enumerate(replaced):
            if not val:
                result[i] = s[i]

        return "".join(result)
