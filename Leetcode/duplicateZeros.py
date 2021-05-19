'''
Question link:https://leetcode.com/problems/duplicate-zeros/


Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.


'''


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dups=0
        lenOfarr=len(arr)
        i=0
        arr2=[]
        for i in arr:
            if dups>=lenOfarr:
                break
            if i==0:
                arr2.append(0)
                arr2.append(0)
                dups+=2
            else:
                arr2.append(i)
                dups+=1
        arr[:]=arr2[:lenOfarr]
