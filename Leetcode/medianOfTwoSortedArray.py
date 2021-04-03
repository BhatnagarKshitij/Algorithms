'''
Question link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       # c=list() #Empty List
        #c.extend(nums1) #Extend List nums1
        nums1.extend(nums2) #Extend List nums2
        nums1.sort() #uild-in sort function to sort array
        ans=None 
        length=len(nums1) #length of merged sorted list
        
        if length % 2 == 0: #Even
            ans=(nums1[int(length/2)-1]+nums1[int(length/2)])/2
        else: #Odd
            ans=nums1[int(length/2)]
            
        return ans
