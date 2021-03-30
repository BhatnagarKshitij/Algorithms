'''
Question link: https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        '''
    Solution-1
        sep=0
        parity=[]
        for num in A:
            if num%2==0:
                parity.insert(sep,num)
                sep+=1
            else:
                parity.append(num)
        return parity
        '''
#Solution2
        even=[]
        odd=[]
        
        for num in A:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd
