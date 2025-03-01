# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# My solution:
# class Solution {
#     public int majorityElement(int[] nums) {
#         Map<Integer, Integer> map = new HashMap<>();
#         for (int num : nums) {
#             Integer integer = map.get(num);
#             int m = integer == null ? 1: integer + 1;
#             map.put(num, m);
#         }
#         for (Map.Entry<Integer, Integer> e : map.entrySet()) {
#             if (e.getValue() >= (int) Math.ceil((double) nums.length / 2)) {
#                 return e.getKey();
#             }
#         }
#         return 0;
#     }
# }
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate