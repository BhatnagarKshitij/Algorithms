'''
Problem Statement: 
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Question Link: https://leetcode.com/problems/rotate-image/

'''

class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
#         ## METHOD-1 #LESS OPTIMIZED ##
        
#         lengthOfMatrix=len(matrix)
#         if lengthOfMatrix <=1:
#             return matrix
#         
#         matrix.reverse()
#         column=0
#         row=0
#         columnRunner=-1
#         rowRunner=-1
#         while row!=lengthOfMatrix:
#             rowRunner+=1
#             columnRunner+=1
#             temp=matrix[columnRunner][column]
#             matrix[columnRunner][column]=matrix[row][rowRunner]
#             matrix[row][rowRunner]=temp
#             if rowRunner==lengthOfMatrix-1:
#                 row+=1
#                 column+=1
#                 rowRunner=row-1
#                 columnRunner=column-1
#         print(matrix)

#       ##  METHOD-2 OPTIMIZED ##
        
        lengthOfMatrix=len(matrix)
        common=0
        row,col=0,0
        while(common!=lengthOfMatrix):
            matrix[common][row],matrix[col][common]=matrix[col][common],matrix[common][row]
            row+=1
            col+=1
            if row==lengthOfMatrix:
                common+=1
                row=common
                col=common
        for items in matrix:
            items.reverse()
        print(matrix)
        
solution=Solution()
#print(solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print(solution.rotate([[1,2,3],[4,5,6],[7,8,9]]))
