from typing import List

"""
Find Minimum in Rotated Sorted List

Approach
--------
The brute force solution to this problem is to do a linear scan of the list
and find the minimum. This solution is O(n) time an O(1) space. However, given
that we have a sorted array, we know we can optimize this via binary search
to reduce run time complexity to O(lg n).

To find the minimum value in a rotated sorted list, we need to use a variation
of binary search. For this solution, we change the loop invariant which is typically
doing something like left <= right, but for this solution we limit this to left < right.

Pseudocode
----------
left, right = 0, n

while left < right:
    mid = (left + right) // 2

    # The reason we're using this condition is because
    # if the number in the middle is currently greater than the
    # value at the end, then this means that the rotation is on the left
    # of mid so we have to limit our search space there
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        # otherwise, we assign mid to right.
        right = mid
"""
def find_min_in_rotated_sorted_list(nums: List[int]) -> int:
    n = len(nums)
    left, right = 0, n - 1

    while left < right:
        mid = left + ((right - left) >> 1)

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
