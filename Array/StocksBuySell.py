class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lengthOfPrices=len(prices)
        
        if lengthOfPrices<=1:
            return 0
        
        buy=False
        maxProfit=0
        pointer=1
        
        while pointer!=lengthOfPrices:
            if prices[pointer-1] > prices[pointer]:
                if buy is not False:
                    maxProfit+=prices[pointer-1]-buy
                    buy=False
            else:
                if buy is False:
                    buy=prices[pointer-1]
            pointer+=1
        if buy is not False and buy!=prices[pointer-1]:
            maxProfit+=prices[pointer-1]-buy
        
        return maxProfit
                

solution=Solution()
print(solution.maxProfit([3,3,5,0,0,3,1,4]))