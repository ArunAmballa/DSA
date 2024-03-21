class Solution:
    def helper(self,i,j,n,triangle,dp):
        if i==n:
            return triangle[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        down=triangle[i][j]+self.helper(i+1,j,n,triangle,dp)
        downRight=triangle[i][j]+self.helper(i+1,j+1,n,triangle,dp)
        dp[i][j]=min(down,downRight)
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        m=len(triangle[n-1])
        prev=[0 for j in range(m)]
        for i in range(n-1,-1,-1):
            temp=[0]*m
            for j in range(i,-1,-1):
                if i==n-1:
                    temp[j]=triangle[i][j]
                else:
                    down=triangle[i][j]+prev[j]
                    downRight=triangle[i][j]+prev[j+1]
                    temp[j]=min(down,downRight)
            prev=temp
        return prev[0]


    
        