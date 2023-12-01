from queue import Queue
class Solution:
    def bfs(self,q,visited,grid):
        r=len(grid)
        c=len(grid[0])
        while not q.empty():
            i,j=q.get()
            if i-1>=0 and grid[i-1][j]==1 and visited[i-1][j]==0:
                q.put([i-1,j])
                visited[i-1][j]=1   
            if i+1<r and grid[i+1][j]==1 and visited[i+1][j]==0:
                q.put([i+1,j])
                visited[i+1][j]=1
            if j-1>=0 and grid[i][j-1]==1 and visited[i][j-1]==0:
                q.put([i,j-1])
                visited[i][j-1]=1
            if j+1<c and grid[i][j+1]==1 and visited[i][j+1]==0:
                q.put([i,j+1])
                visited[i][j+1]=1
                
    def numEnclaves(self, grid: List[List[int]]) -> int:
        visited=[[0 for j in range(len(grid[i]))]for i in range(len(grid))]
        q=Queue()
        r=len(grid)
        c=len(grid[0])
        for i in range(0,len(grid)):
            for j in range(len(grid[i])):
                if i==0 or j==0 or i==r-1 or j==c-1:
                    if grid[i][j]==1:
                        q.put([i,j])
                    visited[i][j]=1
        self.bfs(q,visited,grid)
        cnt=0
        print(visited)
        print(grid)
        for i in range(len(visited)):
            for j in range(len(visited[i])):
                if visited[i][j]==0 and grid[i][j]==1:
                    cnt=cnt+1
        return cnt

        