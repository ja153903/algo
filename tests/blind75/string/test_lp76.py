from ....src.blind75.string.lp76 import Solution


solution = Solution()


def test_lp76_case1():
    assert solution.minWindow("ADOBECODEBANC", "ABC") in ["BANC"]


def test_lp76_case2():
    assert solution.minWindow("a", "a") in ["a"]
