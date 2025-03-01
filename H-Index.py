# 274. H-Index
# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
# Example 1:
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:
#
# Input: citations = [1,3,1]
# Output: 1
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        p = [0] * (n + 1)
        for i in citations:
            p[i if i <= n else n] += 1
        h = 0
        for i in range(n, -1, -1):
            h += p[i]
            if h >= i:
                return i
        return 0