'''
Question Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numbersIntersect=[]
        number={}
        
        for data in nums1:
            number[data]= 1 if number.get(data) is None else number[data] + 1
        
        for data in nums2:
            dataInDict=number.get(data)
            if dataInDict is not None:
                if dataInDict>1:
                    number[data]-=1
                else:
                    number.pop(data)
                numbersIntersect.append(data)
                
        return numbersIntersect
    
solution=Solution()
print(solution.intersect([1,2,2,1],[2,2]))
