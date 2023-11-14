class Solution:
    # def helper(self,m,n,dp):
    #     if m<0 or n<0:
    #         return 0
    #     if m==0 or n==0:
    #         return 1
    #     if dp[m][n]!=-1:
    #         return dp[m][n]
    #     dp[m][n]=self.helper(m-1,n,dp)+self.helper(m,n-1,dp)
    #     return dp[m][n]
    def uniquePaths(self, m: int, n: int) -> int:
        # dp=[[-1 for j in range(n)]for i in range(m)]
        # return self.helper(m-1,n-1,dp)
        prev=[-1]*(n)
        for i in range(m):
            curr=[-1]*(n)
            for j in range(n):
                if i<0 or j<0:
                    curr[j]=0
                    continue
                if i==0 or j==0:
                    curr[j]=1
                    continue
                curr[j]=prev[j]+curr[j-1]
            prev=curr
        return curr[n-1]


        