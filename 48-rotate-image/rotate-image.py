class Solution:
    def reverse(self,i,j,arr):
        while i<=j:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
            j=j-1
        return
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)-1
        for i in range(0,n+1):
            for j in range(i+1,n+1):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            self.reverse(0,n,matrix[i])
        
        