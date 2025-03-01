# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return output
            s = strs[0][i]
            for str in strs:
                if i >= len(str) or str[i] != s:
                    return output
            output += s
            i += 1


if __name__ == '__main__':
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
