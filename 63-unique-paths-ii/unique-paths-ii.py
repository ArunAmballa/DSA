class Solution:
    # def helper(self,n,m,obstacleGrid):
    #     if obstacleGrid[n][m]==1:
    #         return 0
    #     if n<0 or m<0:
    #         return 0
    #     if n==0 and m==0:
    #         return 1
    #     return self.helper(n-1,m,obstacleGrid)+self.helper(n,m-1,obstacleGrid)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        prev=[0]*(m)
        for i in range(0,n):
            curr=[0]*(m)
            for j in range(0,m):
                if obstacleGrid[i][j]==1:
                    curr[j]=0
                    continue
                if i<0 or j<0:
                    curr[j]=0
                    continue
                if i==0 and j==0:
                    curr[j]=1
                    continue
                curr[j]=prev[j]+curr[j-1]
            prev=curr
        return curr[m-1]
