class Solution:
    def helper(self,i,j,triangle,n,dp):
        if i==n-1:
            return triangle[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]=triangle[i][j]+min(self.helper(i+1,j,triangle,n,dp),self.helper(i+1,j+1,triangle,n,dp))
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[-1 for j in range(len(triangle))]for i in range(len(triangle))]
        # return self.helper(0,0,triangle,len(triangle),dp)
        n=len(triangle)
        for j in range(0,n):
            dp[n-1][j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j]=triangle[i][j]+min(dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]