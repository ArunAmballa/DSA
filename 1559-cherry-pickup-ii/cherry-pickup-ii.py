class Solution:
    def helper(self,i,j1,j2,n,m,grid,dp):
        if j1<0 or j2<0 or j1>=m or j2>=m:
            return -int(1e9)
        if i==n-1:
            if j1==j2:
                return grid[i][j1]
            else:
                return grid[i][j1]+grid[i][j2]
        if dp[i][j1][j2]!=-1:
            return dp[i][j1][j2]
        maxi=-int(1e9)
        for dj1 in range(-1,2):
            for dj2 in range(-1,2):
                if j1==j2:
                    maxi=max(maxi,grid[i][j1]+self.helper(i+1,j1+dj1,j2+dj2,n,m,grid,dp))
                else:
                    maxi=max(maxi,grid[i][j1]+grid[i][j2]+self.helper(i+1,j1+dj1,j2+dj2,n,m,grid,dp))
        dp[i][j1][j2]=maxi
        return dp[i][j1][j2]
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[[-1 for j in range(m)]for j in range(m)]for i in range(n)]
        return self.helper(0,0,m-1,n,m,grid,dp)
        