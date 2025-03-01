# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
#
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
#
# Output: true
#
# Explanation:
#
# The bijection can be established as:
#
# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:
#
# Input: pattern = "abba", s = "dog cat cat fish"
#
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
#
# Output: false
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        if len(s_words) != len(pattern):
            return False
        dic = {}
        dic2 = {}
        for i in range(len(s_words)):
            if s_words[i] in dic and dic[s_words[i]] != pattern[i]:
                return False
            if s_words[i] not in dic:
                dic[s_words[i]] = pattern[i]

            if pattern[i] in dic2 and dic2[pattern[i]] != s_words[i]:
                return False
            if pattern[i] not in dic2:
                dic2[pattern[i]] = s_words[i]
        return True
