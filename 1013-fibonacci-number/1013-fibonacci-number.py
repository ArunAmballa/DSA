class Solution:
    def fibDP(self,n,dp):
        if n==0 or n==1:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fibDP(n-1,dp)+self.fibDP(n-2,dp)
        return dp[n]

    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.fibDP(n,dp)
        