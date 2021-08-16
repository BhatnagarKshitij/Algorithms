class Solution(object):
    def pivotIndex(self, nums):
        leftSum=0
        sumOfArray=sum(nums)
        
        for index,value in enumerate(nums):
            if leftSum==sumOfArray-(leftSum+value):
                return index
            leftSum+=value
        return -1
