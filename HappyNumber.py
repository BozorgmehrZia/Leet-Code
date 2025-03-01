# 202. Happy Number
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
#
#
# Example 1:
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# Example 2:
#
# Input: n = 2
# Output: false
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            return sum(int(x) ** 2 for x in str(num))

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1


class Solution2:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def get_next_number(n):
            output = 0

            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10

            return output

        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True

        return False