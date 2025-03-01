# 162. Find Peak Element
# Medium
# Topics
# Companies
# A peak element is an element that is strictly greater than its neighbors.
#
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        end = n - 1
        if n == 1:
            return 0
        while start <= end:
            m = (end + start) // 2
            if (m == 0 and nums[m + 1] < nums[m]) or (m == n - 1 and nums[m - 1] < nums[m]) or nums[m - 1] < nums[m] > nums[m + 1]:
                return m
            if nums[m + 1] >= nums[m]:
                start = m + 1
            else:
                end = m - 1
        return m
