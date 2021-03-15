'''
Question link: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        oldLength=len(nums)
        newLength=len(set(nums))
        return False if oldLength == newLength else True
solution=Solution()
print(solution.containsDuplicate([]))
