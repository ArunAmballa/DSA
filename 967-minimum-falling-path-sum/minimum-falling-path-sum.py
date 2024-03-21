class Solution:
    def helper(self,n,m,matrix,c,dp):
        if m<0 or m>=c:
            return 1<<31
        if n==0:
            return matrix[n][m]
        if dp[n][m]!=-1:
            return dp[n][m]
        top=matrix[n][m]+self.helper(n-1,m,matrix,c,dp)
        topRight=matrix[n][m]+self.helper(n-1,m+1,matrix,c,dp)
        topLeft=matrix[n][m]+self.helper(n-1,m-1,matrix,c,dp)
        dp[n][m]=min(top,min(topLeft,topRight))
        return dp[n][m]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans=1<<31
        n=len(matrix)
        m=len(matrix[0])
        prev=[0 for j in range(m)]
        for i in range(0,n):
            temp=[0]*m
            for j in range(0,m):
                if i==0:
                    temp[j]=matrix[i][j]
                else:
                    top=matrix[i][j]+prev[j]
                    if j+1<n:
                        topRight=matrix[i][j]+prev[j+1]
                    else:
                        topRight=1<<31
                    if j-1>=0:
                        topLeft=matrix[i][j]+prev[j-1]
                    else:
                        topLeft=1<<31
                    temp[j]=min(top,min(topLeft,topRight))
            prev=temp
        for j in range(0,m):
            ans=min(ans,prev[j])            
        return ans
        
        