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
        dp=[[-1 for j in range(m)]for i in range(n)]
        return self.helper(n-1,m-1,grid,dp)
        