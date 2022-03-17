from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        initialize i = 0
        go through each string in the array check if they're the same char at i
        if not, then return previous result
        """
        prefix = []
        min_len = len(min(strs, key=lambda s: len(s)))

        for i in range(min_len):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                if ch != strs[j][i]:
                    return "".join(prefix)

            prefix.append(ch)

        return "".join(prefix)
