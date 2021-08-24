class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputArray=[1]*len(nums)
        lenOfNums=len(nums)
        for i in range(1,lenOfNums):
            outputArray[i]=nums[i-1]*outputArray[i-1]
        
        totalProduct=1
        
        for i in range(lenOfNums-1,-1,-1):
            outputArray[i]*=totalProduct
            totalProduct*=nums[i]
        return outputArray
        
