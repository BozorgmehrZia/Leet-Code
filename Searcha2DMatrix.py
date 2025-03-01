# 74. Search a 2D Matrix
# You are given an m x n integer matrix matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_row(matrix):
            start = 0
            end = len(matrix) - 1
            while start <= end:
                m = (end + start) // 2
                if matrix[m][0] < target:
                    if m == len(matrix) - 1 or matrix[m + 1][0] > target:
                        return m
                    start = m + 1
                elif matrix[m][0] == target:
                    return m
                else:
                    end = m - 1
            return m

        m = get_row(matrix)
        start = 0
        end = len(matrix[m]) - 1
        while start <= end:
            n = (end + start) // 2
            if matrix[m][n] < target:
                start = n + 1
            elif matrix[m][n] == target:
                return True
            else:
                end = n - 1

        return matrix[m][n] == target


if __name__ == '__main__':
    Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11)
    Solution().searchMatrix([[1]], 1)
