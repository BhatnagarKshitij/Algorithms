'''
Question link: https://leetcode.com/problems/maximum-69-number/

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        num=str(num)
        return num.replace('6','9',1)
                
