class Solution:
    def moveZeroes(self, nums):
#         for data in nums:
#             if data is 0:
#                 nums.remove(data)
#                 nums.append(0)
#         return nums

#         lenOfNums=len(nums)
#         p=0
#         n=0
#         while n!=lenOfNums:
#             if nums[n] is 0:
#                 n+=1
#             else:
#                 temp=nums[n]
#                 nums[n]=0
#                 nums[p]=temp
#                 p+=1
#                 n+=1
#         print(nums)
            
            
        
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero = non_zero + 1
                
                
solution=Solution()
print(solution.moveZeroes([0,1,0,3,12]))