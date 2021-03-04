class Solution:
    def singleNumber(self, nums):
        current = 0
        for n in nums:
            current = current ^ n
            
        return current

solution=Solution()
print(solution.singleNumber([1,1,6,6,8,6,6,4,4]))