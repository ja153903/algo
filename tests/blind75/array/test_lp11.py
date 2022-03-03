from ....src.blind75.array.lp11 import Solution


solution = Solution()


def test_lp11_case1():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height) == 49


def test_lp11_case2():
    height = [1, 1]
    assert solution.maxArea(height) == 1
