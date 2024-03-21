class Solution:
    def helper(self,n,m,matrix,c,dp):
        if m<0 or m>=c:
            return 1<<31
        if n==0:
            return matrix[n][m]
        if dp[n][m]!=-1:
            return dp[n][m]
        top=matrix[n][m]+self.helper(n-1,m,matrix,c,dp)
        topRight=matrix[n][m]+self.helper(n-1,m+1,matrix,c,dp)
        topLeft=matrix[n][m]+self.helper(n-1,m-1,matrix,c,dp)
        dp[n][m]=min(top,min(topLeft,topRight))
        return dp[n][m]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans=1<<31
        n=len(matrix)
        m=len(matrix[0])
        dp=[[-1 for j in range(m)]for i in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                if i==0:
                    dp[i][j]=matrix[i][j]
                else:
                    top=matrix[i][j]+dp[i-1][j]
                    if j+1<n:
                        topRight=matrix[i][j]+dp[i-1][j+1]
                    else:
                        topRight=1<<31
                    if j-1>=0:
                        topLeft=matrix[i][j]+dp[i-1][j-1]
                    else:
                        topLeft=1<<31
                    dp[i][j]=min(top,min(topLeft,topRight))
        for j in range(0,m):
            ans=min(ans,dp[n-1][j])            
        return ans
        
        