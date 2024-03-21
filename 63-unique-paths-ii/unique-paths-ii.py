class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0 for j in range(m)]for i in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    dp[i][j]=1
                else:
                    top=0
                    left=0
                    if i>0:
                        top=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=top+left
        return dp[n-1][m-1]

        