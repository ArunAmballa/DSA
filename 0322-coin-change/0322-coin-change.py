class Solution:
    def helper(self,n,w,dp,wt):
        if w==0:
            return 0
        if n==0:
            return 1<<31
        if dp[n][w]!=-1:
            return dp[n][w]
        if wt[n-1]<=w:
            dp[n][w]=min((1+self.helper(n,w-wt[n-1],dp,wt)),self.helper(n-1,w,dp,wt))
        else:
            dp[n][w]=self.helper(n-1,w,dp,wt)
        return dp[n][w]

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1 for j in range(amount+1)]for i in range(len(coins)+1)]
        # ans=self.helper(len(coins),amount,dp,coins)
        # if ans>amount:
        #     return -1
        # return ans
        
        n = len(coins)
        w = amount
        wt = coins
        prev = [0] + [float('inf')] * amount  

        for i in range(1, n + 1):
            curr = [0] * (amount + 1)
            for j in range(amount + 1):
                if j == 0:
                    curr[j] = 0
                    continue
                if wt[i - 1] <= j:
                    curr[j] = min(1 + curr[j - wt[i - 1]], prev[j])
                else:
                    curr[j] = prev[j]
            prev = curr

        return -1 if curr[w] == float('inf') else curr[w]

        