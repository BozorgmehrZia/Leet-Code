class Solution:
    def gcdOfStrings(self,str1: str, str2: str) -> str:
                # Helper function to check if str1 can be formed by repeating pattern str2
        def is_divisible(str1, str2):
            if len(str1) % len(str2) != 0:
                return False
            return str1 == str2 * (len(str1) // len(str2))

    # Find the greatest common divisor of the lengths of str1 and str2
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
