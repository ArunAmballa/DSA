class Solution:
    def helper(self,m,n,dp):
        if m==0 and n==0:
            return 1
        if m<0 or n<0:
            return 0
        if dp[m][n]!=-1:
            return dp[m][n]
        dp[m][n]=self.helper(m-1,n,dp)+self.helper(m,n-1,dp)
        return dp[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for j in range(n)]for i in range(m)]
        # return self.helper(m-1,n-1,dp)
        for i in range(m):
            for j in range(n):
                if i<0 or j<0:
                    dp[i][j]=0
                    continue
                if i==0 or j==0:
                    dp[i][j]=1
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]


        