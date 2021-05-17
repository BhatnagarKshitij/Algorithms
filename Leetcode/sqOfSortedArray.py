'''
Question link: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/


Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
         return(sorted([x*x for x in nums]))
