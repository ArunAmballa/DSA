class Solution:
    def helper(self,i,j,triangle,n,dp):
        if i==n-1:
            return triangle[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j]=triangle[i][j]+min(self.helper(i+1,j,triangle,n,dp),self.helper(i+1,j+1,triangle,n,dp))
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        prev=[0]*(n)
        for j in range(0,n):
            prev[j]=triangle[n-1][j]
        for i in range(n-2,-1,-1):
            curr=[0]*n
            for j in range(i,-1,-1):
                curr[j]=triangle[i][j]+min(prev[j],prev[j+1])
            prev=curr
        return prev[0]