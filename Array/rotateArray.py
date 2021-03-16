'''
Question link: https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotateCount=k%len(nums)
        return nums[-rotateCount:]+nums[:-rotateCount]
        
    
solution=Solution()
print(solution.rotate([-1,-100,3,99],2))
