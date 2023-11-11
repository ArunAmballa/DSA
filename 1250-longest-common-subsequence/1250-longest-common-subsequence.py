class Solution:
    def helper(self,x,y,n,m,dp):
        if n==0 or m==0:
            return 0
        if dp[n][m]!=-1:
            return dp[n][m]
        if x[n-1]==y[m-1]:
            dp[n][m]=1+self.helper(x,y,n-1,m-1,dp)
        else:
            dp[n][m]=max(self.helper(x,y,n,m-1,dp),self.helper(x,y,n-1,m,dp))
        return dp[n][m]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1 for j in range(m+1)]for i in range(n+1)]
        return self.helper(text1,text2,n,m,dp)

        