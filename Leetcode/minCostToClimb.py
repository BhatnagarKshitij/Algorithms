class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lengthOfStairs=len(cost)
        dp=[None]*len(cost)
        
        dp[0],dp[1]=cost[0],cost[1]
        
        for i in range(2,lengthOfStairs):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
            
        return min(dp[lengthOfStairs-1],dp[lengthOfStairs-2])
                
