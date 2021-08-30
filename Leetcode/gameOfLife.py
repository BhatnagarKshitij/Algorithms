class Solution:
    def countOnes(self,board,i,j):
        ones=0
        #TOP
        if i-1>=0 and abs(board[i-1][j])==1:
            ones+=1
        #TOP RIGHT
        if i-1>=0 and j+1<len(board[0]) and abs(board[i-1][j+1])==1:
            ones+=1
        #RIGHT
        if j+1<len(board[0]) and abs(board[i][j+1])==1:
            ones+=1
        #RIGHT BOTTOM
        if i+1<len(board) and j+1<len(board[0]) and abs(board[i+1][j+1])==1:
            ones+=1
        #BOTTOM
        if i+1<len(board) and abs(board[i+1][j])==1:
            ones+=1
        #BOTTOM LEFT
        if i+1<len(board) and j-1>=0 and abs(board[i+1][j-1])==1:
            ones+=1
        #LEFT
        if j-1>=0 and abs(board[i][j-1])==1:
            ones+=1
        #LEFT TOP
        if i-1>=0 and j-1>=0 and abs(board[i-1][j-1])==1:
            ones+=1

        return ones
    
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                ones=self.countOnes(board,i,j)
                if board[i][j]==1:
                    if ones<2:
                        board[i][j]=-1
                    elif ones>3:
                        board[i][j]=-1
                else:
                    if ones==3:
                        board[i][j]=2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==2:
                    board[i][j]=1
                elif board[i][j]==-1:
                    board[i][j]=0

