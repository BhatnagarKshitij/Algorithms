'''
QUESTOIN LINK: https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
'''
class Solution:
    def isValidSudoku(self, board):
        rows=[{} for i in range(9)]
        columns=[{} for i in range(9)]
        boxes=[{} for i in range(9)]
        breakSolution=False
        
        for i in range(9):
            for j in range(9):
                num=board[i][j]
                if num is ".":
                    continue
                #Check For Row
                rows[i][num]=rows[i].get(num,0)+1   
                #Check for column
                columns[j][num]=columns[j].get(num,0)+1
                #Check for box
                boxNumber=(int(i/3))*3+int(j/3)                
                boxes[boxNumber][num]=boxes[boxNumber].get(num,0)+1
                
                if columns[j].get(num)>1 or rows[i].get(num)>1 or boxes[boxNumber].get(num)>1:
                    return False

        return True
solution=Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".",".","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,["",".",".",".","8",".",".","7","9"]]))