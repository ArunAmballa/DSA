class Solution:
    def helper(self,n,m,grid,dp):
        if n==0 and m==0:
            return grid[n][m]
        if n<0 or m<0:
            return (1<<31)-1
        if dp[n][m]!=-1:
            return dp[n][m]
        top=grid[n][m]+self.helper(n-1,m,grid,dp)
        left=grid[n][m]+self.helper(n,m-1,grid,dp)
        dp[n][m]=min(top,left)
        return dp[n][m]
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[0 for j in range(m)]for i in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    if i>0:
                        top=grid[i][j]+dp[i-1][j]
                    else:
                        top=1<<31
                    if j>0:
                        left=grid[i][j]+dp[i][j-1]
                    else:
                        left=1<<31
                    dp[i][j]=min(top,left)
        return dp[n-1][m-1]
        