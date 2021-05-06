'''
Question link: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

Given an integer n, return any array containing n unique integers such that they add up to 0.

'''

class Solution:
    def sumZero(self, n: int) -> List[int]:
        r=[]
        sum=0
        for i in range(1,n):
            sum+=i
            r.append(i)
        else:
            r.append(-sum)
        return r
