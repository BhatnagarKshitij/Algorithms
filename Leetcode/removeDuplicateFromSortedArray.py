class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        pointer=None
        lastValue=nums[0]

        for i in range(1,len(nums)):
            if lastValue!=nums[i]:
                if pointer:
                    nums[pointer]=nums[i]
                    pointer+=1
                lastValue=nums[i]
            else:
                if not pointer:
                    pointer=i
        return pointer
