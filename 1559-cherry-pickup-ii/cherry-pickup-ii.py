class Solution:
    def maxPickup(self,i,j1,j2,grid,dp):
            if j1 < 0 or j2 < 0 or j1 >= len(grid[0]) or j2 >= len(grid[0]): return -1e8
            if (dp[i][j1][j2] != -1): return dp[i][j1][j2]
            if (i == len(grid)-1):
                if (j1 == j2): return grid[i][j1]
                else: return grid[i][j1] + grid[i][j2]
            maxi = -1e8
            for dj1 in range(-1,2):
                for dj2 in range(-1,2):
                    value = 0
                    if (j1 == j2):
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]
                    value += self.maxPickup(i+1,j1+dj1,j2+dj2,grid,dp)
                    maxi = max(maxi,value)
            dp[i][j1][j2] = maxi
            return dp[i][j1][j2]
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) 
        dp = [[[-1 for i in range(m+1)] for j in range(m+1)] for k in range(n+1)]
        return self.maxPickup(0,0,m-1,grid,dp)