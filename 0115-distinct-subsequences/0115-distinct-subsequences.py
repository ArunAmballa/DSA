class Solution:
    def lcs(self,x,y,n,m,dp):
        if (n==0 and m==0):
            return 1
        if m==0:
            return 1
        if n==0:
            return 0
        if dp[n][m]!=-1:
            return dp[n][m]
        if x[n-1]==y[m-1]:
            dp[n][m]=self.lcs(x,y,n-1,m,dp)+self.lcs(x,y,n-1,m-1,dp)
        else:
            dp[n][m]=self.lcs(x,y,n-1,m,dp)
        return dp[n][m]
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[-1 for j in range(len(t)+1)]for i in range(len(s)+1)]
        return self.lcs(s,t,len(s),len(t),dp)