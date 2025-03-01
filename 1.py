class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
       len1 = len(word1)
       len2 = len(word2)
       pt1 = 0
       pt2 = 0
       res = ''
       while pt1 !=len1 or pt2 != len2:
            if pt1 < len1:
                res += word1[pt1]
                pt1+=1
            if pt2 < len2 :
                res += word2[pt2]
                pt2+=1
       return res#!/usr/bin/env wolframscript
