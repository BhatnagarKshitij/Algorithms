'''
Question link: https://leetcode.com/problems/length-of-last-word/


Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if len(s.split()) == 0 else len(s.split()[-1])
