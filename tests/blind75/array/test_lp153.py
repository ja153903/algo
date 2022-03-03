from ....src.blind75.array.lp153 import Solution


solution = Solution()


def test_lp153_case1():
    nums = [3, 4, 5, 1, 2]
    assert solution.findMin(nums) == 1
