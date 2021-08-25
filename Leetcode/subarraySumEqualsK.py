class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap={}
        hashMap[0]=1
        totalSum=0
        result=0

        for value in nums:
            totalSum+=value
            if (totalSum - k) in hashMap:
                result+=hashMap.get(totalSum - k)
            hashMap[totalSum]=hashMap.get(totalSum,0)+1
        return result
