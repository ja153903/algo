from ....src.blind75.array.lp1 import Solution


solution = Solution()


def test_lp1_case1():
    nums = [2, 7, 11, 15]
    target = 9

    assert solution.twoSum(nums, target) == [0, 1]
