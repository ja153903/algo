class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        Given two strings s and part, perform the following operation
        on  s until all occurences of the substring part are removed.
        Find the leftmost occurence of the substring part and remove it from s.

        Return s after removing all occurences of part
        """
        n = len(part)

        while (start := s.find(part)) != -1:
            filtered = []
            for i, ch in enumerate(s):
                if start <= i < start + n:
                    continue

                filtered.append(ch)
            s = "".join(filtered)

        return s

    def optimal(self, s: str, part: str) -> str:
        pass
