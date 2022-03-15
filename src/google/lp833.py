from typing import List


"""
Perform some operations on the result.

if the substring sources[i] occurs at index indices[i], then we replace the string
"""
class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        changes = []

        for idx, src, target in zip(indices, sources, targets):
            changes.append((idx, src, target))

        changes.sort(key=lambda tup: tup[0])

        result = []

        i, j = 0, 0

        while i < len(s) and j < len(changes):
            idx, src, target = changes[j]
            while i < idx:
                result.append(s[i])
                i += 1

            current_substr = s[idx:idx + len(src)]
            j += 1

            if current_substr == src:
                result.append(target)
                i += len(src)

        while i < len(s):
            result.append(s[i])
            i += 1

        return "".join(result)

