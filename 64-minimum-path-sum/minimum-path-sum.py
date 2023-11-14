class Solution:
    def helper(self,n,m,grid,dp):
        if n<0 or m<0:
            return 1<<31
        if n==0 and m==0:
            return grid[n][m]
        if dp[n][m]!=-1:
            return dp[n][m]
        dp[n][m]=grid[n][m]+min(self.helper(n-1,m,grid,dp),self.helper(n,m-1,grid,dp))
        return dp[n][m]
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for j in range(m)]for i in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                    continue
                up=dp[i-1][j] if i-1>=0 else 1<<31
                left=dp[i][j-1] if j-1>=0 else 1<<31
                dp[i][j]=grid[i][j]+min(up,left)
        return dp[n-1][m-1]
        