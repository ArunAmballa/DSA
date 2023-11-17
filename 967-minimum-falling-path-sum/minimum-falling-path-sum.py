class Solution:
    def helper(self,i,j,matrix,n,dp):
        if j<0 or j>=n:
            return 1<<31
        if i==0:
            return matrix[0][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        left=matrix[i][j]+self.helper(i-1,j-1,matrix,n,dp)
        down=matrix[i][j]+self.helper(i-1,j,matrix,n,dp)
        right=matrix[i][j]+self.helper(i-1,j+1,matrix,n,dp)
        dp[i][j]=min(left,min(down,right))
        return dp[i][j]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans=1<<31
        n=len(matrix)
        dp=[[0 for j in range(n)]for i in range(n)]
        for j in range(n):
            dp[0][j]=matrix[0][j]
        for i in range(1,n):
            for j in range(0,n):
                left=matrix[i][j]+(dp[i-1][j-1] if j-1>=0 else 1<<31)
                down=matrix[i][j]+(dp[i-1][j])
                right=matrix[i][j]+(dp[i-1][j+1] if j+1<n else 1<<31)
                dp[i][j]=min(left,min(down,right))
        for j in range(0,n):
            ans=min(ans,dp[n-1][j])
        return ans
            
        