'''
Question link: https://leetcode.com/problems/determine-if-string-halves-are-alike/

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt, half = 0, len(s) / 2
        vowel=set("AEIOU")
        for i, c in enumerate(s):
            if c.upper() in vowel:
                cnt += 1 if i < half else -1 
        return cnt == 0
