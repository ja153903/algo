from ....src.blind75.string.lp5 import Solution

solution = Solution()


def test_lp5_case1():
    assert solution.longestPalindrome("babad") == "bab"
