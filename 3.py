reverse vowels

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        start = 0
        end = len(s) - 1
        s_array = list(s)
        while start < end:
            while s_array[start].lower() not in vowels and start < end:
                start += 1
            while s_array[end].lower() not in vowels and  start < end :
                end -= 1

            s_array[start], s_array[end] = s_array[end], s_array[start]
            start += 1


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):

            if sum(flowerbed[i - 1: i + 2]) == 0:

                flowerbed[i] = 1

                n -= 1

                if n == 0:
                    return True

        return n <= 0

https://github.com/Garvit244/Leetcode/blob/master/100-200q/152.py