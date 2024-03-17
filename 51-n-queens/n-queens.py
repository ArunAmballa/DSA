class Solution:

    def helper(self,n,col,board,ans,leftRow,lowerDiagonal,upperDiagonal):
        if col==n:
            ans.append(board.copy())
            return 
        for row in range(0,n):
            if((row not in leftRow) and (row+col not in lowerDiagonal) and (n-1+col-row not in upperDiagonal)):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                leftRow.add(row)
                lowerDiagonal.add(row+col) 
                upperDiagonal.add(n-1+col-row)
                self.helper(n,col+1,board,ans,leftRow,lowerDiagonal,upperDiagonal)
                leftRow.remove(row)
                lowerDiagonal.remove(row+col) 
                upperDiagonal.remove(n-1+col-row)
                board[row]=board[row][:col]+"."+board[row][col+1:]
                 
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        leftRow=set()
        upperDiagonal=set()
        lowerDiagonal=set()
        board=["."*n for i in range(n)]
        self.helper(n,0,board,ans,leftRow,lowerDiagonal,upperDiagonal)
        return ans
        