'''
Question link: https://leetcode.com/problems/add-digits/

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''


class Solution:
    def addDigits(self, num: int) -> int:
        if num//10==0:
            return num
        def getNewNumber(num):
            newNum=0
            while num:
                newNum+=num%10
                num=num//10
            return newNum
        while num//10!=0:
            num=getNewNumber(num)
        return num 
