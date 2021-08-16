'''
Question link: https://leetcode.com/problems/squares-of-a-sorted-array/submissions/


Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newArray=list()
        for num in nums:
            newArray.append(num*num)
        newArray.sort()
        return newArray
            
