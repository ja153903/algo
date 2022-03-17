class Solution:
    def checkRecord(self, s: str) -> bool:
        """
        The student was absent ('A') for strictly fewer than 2 days total.
        The student was never late ('L') for 3 or more consecutive days.
        """

        a_count = 0

        for ch in s:
            if ch == "A":
                a_count += 1

        return a_count < 2 and s.find("LLL") == -1
