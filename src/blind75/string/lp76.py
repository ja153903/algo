from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # typical start to sliding window
        count = Counter(t)
        start = 0

        target = len(t)
        min_window = ""

        for end in range(len(s)):
            # if we have the value in the counter, then decrease target len
            if count.get(s[end], 0) > 0:
                target -= 1

            # if count is negative then oh well
            count[s[end]] -= 1

            # we have to replenish
            while target == 0:
                # check if current window should be new min_window
                curr_window_len = end - start + 1

                if not min_window or curr_window_len < len(min_window):
                    min_window = s[start : end + 1]

                count[s[start]] += 1

                if count[s[start]] > 0:
                    target += 1

                start += 1

        return min_window

    def brute_force(self, s: str, t: str) -> str:
        """
        Brute Force:
            * Go through all lengths from [n, m] where n = len(t) and m = len(s)
            * Break on first approach
        """
        if s == t:
            return s

        if len(s) < len(t):
            return ""

        m, n = len(s), len(t)

        substr_len = n
        while substr_len <= m:
            for i in range(m - substr_len + 1):
                count = Counter(t)
                substr = s[i : i + substr_len]
                for ch in substr:
                    if count.get(ch, -1) > 0:
                        count[ch] -= 1

                rem = sum(count.values())
                if rem == 0:
                    return substr

            substr_len += 1

        return ""
