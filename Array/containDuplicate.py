class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        oldLength=len(nums)
        newLength=len(set(nums))
        if oldLength==newLength:
            return False
        else:
            return True

solution=Solution()
print(solution.containsDuplicate([]))