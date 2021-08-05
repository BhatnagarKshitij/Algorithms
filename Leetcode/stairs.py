class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        
        prevOne=1
        prevTwo=0
        result=1
        for i in range(n):
            result=prevOne+prevTwo
            prevOne,prevTwo=prevOne+prevTwo,prevOne
        return result
