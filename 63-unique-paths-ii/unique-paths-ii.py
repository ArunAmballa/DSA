class Solution:
    def helper(self,n,m,obstacleGrid,dp):
        if obstacleGrid[n][m]==1:
            return 0
        if n==0 and m==0:
            return 1
        if n<0 or m<0:
            return 0
        if dp[n][m]!=-1:
            return dp[n][m]
        top=self.helper(n-1,m,obstacleGrid,dp)
        left=self.helper(n,m-1,obstacleGrid,dp)
        dp[n][m]=top+left
        return dp[n][m]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[-1 for j in range(m)]for i in range(n)]
        return self.helper(n-1,m-1,obstacleGrid,dp)
        