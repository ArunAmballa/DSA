class Solution:
    def markRow(self,i,matrix):
        m=len(matrix[0])
        for j in range(m):
            if matrix[i][j]!=0:
                matrix[i][j]='s'
    def markColumn(self,j,matrix):
        n=len(matrix)
        for i in range(n):
            if matrix[i][j]!=0:
                matrix[i][j]='s'
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    self.markRow(i,matrix)
                    self.markColumn(j,matrix)
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='s':
                    matrix[i][j]=0
        
        