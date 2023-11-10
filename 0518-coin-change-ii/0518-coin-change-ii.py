class Solution:
    def helper(self,n,w,wt,dp):
        if w==0:
            return 1
        if n==0:
            return 0
        if dp[n][w]!=-1:
            return dp[n][w]
        if wt[n-1]<=w:
            dp[n][w]=self.helper(n,w-wt[n-1],wt,dp)+self.helper(n-1,w,wt,dp)
        else:
            dp[n][w]=self.helper(n-1,w,wt,dp)
        return dp[n][w]

    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[-1 for j in range(amount+1)]for i in range(len(coins)+1)]
        return self.helper(len(coins),amount,coins,dp)
        