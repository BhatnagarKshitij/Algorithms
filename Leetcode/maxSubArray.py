class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax=nums[0]
        
        currentMax=nums[0]
        
        for i in range(1,len(nums)):
            if nums[i]<currentMax+nums[i]:
                currentMax+=nums[i]
            else:
                currentMax=nums[i]
            
            if currentMax>globalMax:
                globalMax=currentMax
        return globalMax
