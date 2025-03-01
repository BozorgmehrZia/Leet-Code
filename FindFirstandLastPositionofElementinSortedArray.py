# 34. Find First and Last Position of Element in Sorted Array
# Medium
# Topics
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
#
# Input: nums = [], target = 0
# Output: [-1,-1]
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(arr, isMin):
            start = 0
            end = len(arr) - 1
            index = -1
            while start <= end:
                m = (start + end) // 2
                if arr[m] < target:
                    start = m + 1
                elif nums[m] > target:
                    end = m - 1
                else:
                    if isMin:
                        index = m if index == -1 else min(index, m)
                        end = m - 1
                    else:
                        index = max(index, m)
                        start = m + 1
            return index
        return [bs(nums, True), bs(nums, False)]
