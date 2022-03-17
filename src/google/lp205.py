class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Two strings are isomorphic if you can create a mapping from one character to another.
        No two characters can be mapped to the same character.

        === approach ===
        use dictionary to keep track of character mapping.
        if a character already exists in the values, make sure that the key also exists and maps accordingly
        otherwise return false
        """
        if len(s) != len(t):
            return False

        mp1 = {}
        mp2 = {}

        for i in range(len(t)):
            if t[i] not in mp1:
                mp1[t[i]] = s[i]
            elif mp1[t[i]] != s[i]:
                return False

            if s[i] not in mp2:
                mp2[s[i]] = t[i]
            elif mp2[s[i]] != t[i]:
                return False

        return True
