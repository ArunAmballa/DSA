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
        prev=[0]*(m)
        for i in range(0,n):
            curr=[0]*(m)
            for j in range(0,m):
                if i==0 and j==0:
                    curr[j]=grid[i][j]
                    continue
                up=prev[j] if i-1>=0 else 1<<31
                left=curr[j-1] if j-1>=0 else 1<<31
                curr[j]=grid[i][j]+min(up,left)
            prev=curr
        return curr[m-1]
        