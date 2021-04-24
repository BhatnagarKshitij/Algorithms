'''
Question link: https://leetcode.com/problems/third-maximum-number/

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        return sorted(nums)[-3]
