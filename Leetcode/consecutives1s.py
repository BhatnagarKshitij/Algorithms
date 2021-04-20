'''
Question link: https://leetcode.com/problems/max-consecutive-ones/

Given a binary array nums, return the maximum number of consecutive 1's in the array.

'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maximum=0
        for value in nums:
            if value==1:
                count+=1
            else:
                if count>maximum:
                    maximum=count
                count=0
        if count>maximum:
            maximum=count
        return maximum
