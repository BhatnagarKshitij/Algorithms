'''
Question Link: https://leetcode.com/problems/richest-customer-wealth/

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer has in the j-th bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxVal=0
        for cust in accounts:
            maxVal=max(maxVal,sum(cust))
        return maxVal
