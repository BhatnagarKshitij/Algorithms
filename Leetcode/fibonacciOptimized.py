'''
Question link: https://leetcode.com/problems/fibonacci-number/

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 


'''


class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n<3:
            return 1
        num1,num2=1,1
        
        for i in range(n-2):
            num1,num2=num2,num1+num2
            
        return num2
