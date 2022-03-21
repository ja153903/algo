from ...src.common.prefix_sums import get_sum_between


def test_get_sum_between():
    nums = [1, 2, 3, 4, 5]
    i, j = 1, 3

    assert get_sum_between(nums, i, j) == 9
    assert get_sum_between(nums, j, i) == 9
