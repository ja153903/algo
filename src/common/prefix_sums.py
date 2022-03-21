from typing import List


"""
Finding the sum between a range of indices

Approach
--------
To find the sum of items between indices i and j, we can store
the running sum within a prefix_sum array and we can implement some
logic to get the sum.

So suppose that we have a prefix_sum array that contains the running
sum of all the numbers within the array. Now, we want to find the sum
of the elements between i and j.

The solution would look like sum = prefix[j] - prefix[i - 1]

The reason we do i - 1 is because we want to make sure that we remove
the sum of items between 0 and i - 1

Analysis
--------
This problem requires O(n) time and O(n) space for the prefix sum array
"""


def get_sum_between(nums: List[int], i: int, j: int) -> int:
    n = len(nums)

    if n == 0:
        return 0

    if i > j:
        i, j = j, i

    prefix_sum = [0] * n

    for k, val in enumerate(nums):
        if k == 0:
            prefix_sum[k] = val
        else:
            prefix_sum[k] = prefix_sum[k - 1] + val

    return prefix_sum[j] - prefix_sum[i - 1]
