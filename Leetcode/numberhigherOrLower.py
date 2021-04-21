'''
Question link: https://leetcode.com/problems/guess-number-higher-or-lower/

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
'''


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        h=n
        while(True):
            x=random.randint(l,h)
            t=guess(x)
            if t==-1:
                h=x 
            elif t==1:
                l=x 
            else:
                return x
#        minLimit=1
#        maxLimit=n
#        
#        while minLimit!=maxLimit:
#            middle=(minLimit+maxLimit)//2
#            guessMiddle=guess(middle)
#            if guessMiddle==0:
#                return middle
#            elif guessMiddle==-1:
#                maxLimit=middle-1
#            elif guessMiddle==1:
#                minLimit=middle+1
#        else:
#            return minLimit
        
