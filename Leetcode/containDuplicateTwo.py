'''
Question link: https://leetcode.com/problems/contains-duplicate-ii/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        mapping=dict()
        
        for index,value in enumerate(nums):
            if mapping.get(value,False) is False:
                mapping[value]=index
            else:
                if abs(mapping.get(value)-index)<=k:
                    return True
                else:
                    mapping[value]=index
        return False
