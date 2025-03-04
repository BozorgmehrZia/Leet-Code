# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMinElement(nums: List[int]) -> int:
            start = 0
            n = len(nums)
            end = n - 1
            while start < end:
                m = (end + start) // 2
                if nums[m] > nums[end]:
                    start = m + 1
                else:
                    end = m
            return start

        mi = findMinElement(nums)
        if target == nums[mi]:
            return mi
        elif target < nums[mi]:
            return -1
        else:
            if target == nums[-1]:
                return len(nums) - 1
            elif target > nums[-1]:
                start = 0
                end = mi - 1
            else:
                start = mi + 1
                end = len(nums) - 1

        while start <= end:
            m = (end + start) // 2
            if nums[m] < target:
                start = m + 1
            elif nums[m] == target:
                return m
            else:
                end = m - 1
        return -1

if __name__ == '__main__':
    Solution().search([5,1,3], 1)