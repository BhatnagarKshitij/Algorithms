'''
Question link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


class Solution:
    def twoSum(self,nums,target):
        data={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in data.keys():
                return (data[diff],i)
            else:
                data[nums[i]]=i
        return None


print(twoSum([8,-7,5,7,3,6,-3,-6,10,-4]))
    
