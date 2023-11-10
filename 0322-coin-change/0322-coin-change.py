class Solution:
    def unboundedk(self,wt,w,n,dp):
        if w==0:
            return 0
        if n==0:
            return 2<<31
        if dp[n][w]!=-1:
            return dp[n][w]
        if wt[n-1]<=w:
            dp[n][w]=min((1+self.unboundedk(wt,w-wt[n-1],n,dp)),self.unboundedk(wt,w,n-1,dp))
        else:
            dp[n][w]=self.unboundedk(wt,w,n-1,dp)
        return dp[n][w] 
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1 for j in range(amount+1)]for i in range(len(coins)+1)]
        ans=self.unboundedk(coins,amount,len(coins),dp)
        if ans>amount:
            return -1
        return ans
        
    