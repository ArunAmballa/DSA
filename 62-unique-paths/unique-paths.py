class Solution:
    def helper(self,n,m,dp):
        if n==0 or m==0:
            return 1
        if dp[n][m]!=-1:
            return dp[n][m]
        top=self.helper(n-1,m,dp)
        left=self.helper(n,m-1,dp)
        dp[n][m]=top+left
        return dp[n][m]
    def uniquePaths(self, n: int, m: int) -> int:
        dp=[[-1 for j in range(m)] for i in range(n)]
        # for i in range(0,n):
        #     for j in range(0,m):
        #         if i==0 and j==0:
        #             dp[i][j]=1
        #             continue
        #         top=dp[i-1][j]
        #         left=dp[i][j-1]
        #         dp[i][j]=top+left

        return self.helper(n-1,m-1,dp)
        