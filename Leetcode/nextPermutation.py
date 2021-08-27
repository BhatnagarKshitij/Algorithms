class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=None
        right=None

        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                left=i
                break
        if left is None:
            nums.sort()
            return nums
        for j in range(len(nums)-1,-1,-1):
            if nums[j]>nums[left]:
                right=j
                break

        nums[left],nums[right]=nums[right],nums[left]
        right=len(nums)-1
        while left < right:
            nums[left+1],nums[right]=nums[right],nums[left+1]
            left+=1
            right-=1
