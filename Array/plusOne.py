'''
Question link: https://leetcode.com/problems/plus-one/

Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
'''
class Solution:
    def plusOne(self, digits):
        
        #METHOD 1
       data=list(map(int,str(int(''.join(map(str,digits)))+1)))
       return data
        #METHOD 2
#          data=""
#         for elem in digits:
#             data+=str(elem)
#         data=list(map(int,str(int(data)+1)))

        
        
                  
    
solution=Solution()
print(solution.plusOne([8,9,9,9]))
