'''
Question Link: https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
'''


class Solution:
    def jump(self, nums):
        jumps = 0
        dest = 0
        prev = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            dest = max(dest, i + nums[i])
            if i == prev:
                prev = dest
                jumps += 1
                if dest >= len(nums) - 1:
                    return jumps
        return jumps
        
solution=Solution()
print(solution.jump([2,3,0,1,4]))