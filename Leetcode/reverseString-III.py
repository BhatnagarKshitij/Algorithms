'''
Question link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


'''


class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        result=[]
        
        for word in words:
            result.append(word[::-1])
            
        return ' '.join(result)
