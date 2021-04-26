'''
Question link: https://leetcode.com/problems/backspace-string-compare/

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        finalS=[]
        finalT=[]
        
        for ch in s:
            if ch=="#":
                try:
                    finalS.pop()
                except:
                    pass
            else:
                finalS.append(ch)
        
        for ch in t:
            if ch=="#":
                try:
                    finalT.pop()
                except:
                    pass
            else:
                finalT.append(ch)
        
        return finalS==finalT
