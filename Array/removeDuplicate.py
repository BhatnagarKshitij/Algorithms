class Solution:
    def removeDuplicates(self, nums):
        nums[:]=list(set(nums))
        return len(nums)
    
            
    
solution=Solution()
print(solution.removeDuplicates([1,1,2]))