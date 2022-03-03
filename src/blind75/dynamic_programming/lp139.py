"""
Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

=== Solution ===
What is the recursive approach for this problem?
Given some starting point, we should then check to see that the accumulation of the string
ends in a word in the word dictionary. We then should both start solutions and continue building.

Something like this:

def f(s: str, words: Set[str], curr: str, idx: int) -> bool:
    if idx == len(s):
        return True
    
    curr += s[idx]

    return curr in words or f(s, words, curr, idx + 1) or f(s, words, "", idx + 1)
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        # NOTE: dp[i] means that there exists a solution up to index i

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(0, i):
                # if there exists a previous solution
                # and from that solution up to i, we have another word in the set,
                # then dp[i] is also true
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
