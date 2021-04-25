'''
Question link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
'''


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add=0
        multiply=1
        
        while n!=0:
            temp=n%10
            multiply*=temp
            add+=temp
            n=n//10
        return multiply-add
