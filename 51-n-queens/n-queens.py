class Solution:
    def isSafe(self,board,col,row,n):
        originalRow=row
        originalCol=col

        while (col>=0):
            if board[row][col]=="Q":
                return False
            col=col-1
        row=originalRow
        col=originalCol
        while (row>=0 and col>=0):
            if board[row][col]=="Q":
                return False
            row=row-1
            col=col-1
        
        row=originalRow
        col=originalCol
        while(row<n and col>=0):
            if board[row][col]=="Q":
                return False
            row=row+1
            col=col-1
        
        return True

    def helper(self,n,col,board,ans):
        if col==n:
            ans.append(board.copy())
            return 
        for row in range(0,n):
            if(self.isSafe(board,col,row,n)):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                self.helper(n,col+1,board,ans)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                 
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=["."*n for i in range(n)]
        self.helper(n,0,board,ans)
        return ans
        