from typing import List


"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m + n))

=== Solution ===
The brute force solution is to merge the two arrays and then find the median
which is O(m + n) time and space

=== Optimal Solution ===
The optimal solution for this problem is rather tricky to think about.

x -> x1, x2, ..., xn => partition this into x1, ..., xi | x_{i+1}, ..., xn where the partition on the left is x_p1 and the other is x_p2
y -> y1, y2, ..., ym => partition this into y1, ..., yk | y_{k+1}, ..., ym where the partition on the left is y_p1 and the other is y_p2

We want to be able to partition x and y such that
len(x_p1) + len(y_p1) == len(x_p2) + len(y_p2)

We can find this partition via binary search.

Note that we want to make sure that xi <= y_{k+1} and yk <= x_{i+1} or max(x_p1, y_p1) <= min(x_p2, y_p2)
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j  = half_len - i

            if i < m and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2

        return -1

