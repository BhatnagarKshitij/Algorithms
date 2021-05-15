'''
Question link: https://leetcode.com/problems/reverse-string-ii/


Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.


'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        keep = ""
        count = 1
        if k>=len(s):
            return s[::-1]
        for i in range (0,len(s),k+k):
            keep += s[i:i+k][::-1]
            keep += s[i+k:i+k+k]
        return keep
