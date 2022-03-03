from ....src.blind75.array.lp33 import Solution


solution = Solution()


def test_lp33_case1():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    assert solution.search(nums, target) == 4


def test_lp33_case2():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3

    assert solution.search(nums, target) == -1


def test_lp33_case3():
    nums = [1]
    target = 0

    assert solution.search(nums, target) == -1
