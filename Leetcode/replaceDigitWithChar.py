'''
Question link: https://leetcode.com/problems/replace-all-digits-with-characters/

You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
'''


class Solution:
    def replaceDigits(self, s: str) -> str:
        result=""
        for idx in range(len(s)):
            if s[idx].isdigit():
                result+=chr(ord(s[idx-1])+int(s[idx]))
            else:
                result+=s[idx]
        return result
