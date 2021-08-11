class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            if buy<prices[i]:
                currentProfit=prices[i]-buy
                if currentProfit>maxProfit:
                    maxProfit=currentProfit
            else:
                buy=prices[i]
        return maxProfit
