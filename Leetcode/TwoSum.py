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
    