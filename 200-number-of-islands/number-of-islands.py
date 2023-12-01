from queue import Queue
class Solution:
    def bfs(self,source,grid):
        q=Queue()
        q.put(source)
        r=len(grid)
        c=len(grid[0])
        while not q.empty():
            i,j=q.get()
            if i-1>=0 and grid[i-1][j]=="1":
                q.put([i-1,j])
                grid[i-1][j]="0"
            if i+1<r and grid[i+1][j]=="1":
                q.put([i+1,j])
                grid[i+1][j]="0"
            if j-1>=0 and grid[i][j-1]=="1":
                q.put([i,j-1])
                grid[i][j-1]="0"
            if j+1<c and grid[i][j+1]=="1":
                q.put([i,j+1])
                grid[i][j+1]="0"
        

    def numIslands(self, grid: List[List[str]]) -> int:
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    cnt=cnt+1
                    grid[i][j]="0"
                    self.bfs([i,j],grid)
        return cnt