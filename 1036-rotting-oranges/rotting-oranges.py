from queue import Queue
class Solution:
    def helper(self,grid):
        q=Queue()
        r=len(grid)
        c=len(grid[0])
        visited=[[0 for j in range(c)]for i in range(r)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    q.put([i,j])
                    visited[i][j]=1
        time=0
        while not q.empty():
            isSpreaded=False
            n=q.qsize()
            for i in range(n):
                ci,cj=q.get()
                if ci-1>=0 and grid[ci-1][cj]==1 and visited[ci-1][cj]==0:
                    isSpreaded=True
                    visited[ci-1][cj]=1
                    grid[ci-1][cj]=2
                    q.put([ci-1,cj])
                if ci+1<r and grid[ci+1][cj]==1 and visited[ci+1][cj]==0:
                    isSpreaded=True
                    visited[ci+1][cj]=1
                    grid[ci+1][cj]=2
                    q.put([ci+1,cj])
                if cj-1>=0 and grid[ci][cj-1]==1 and visited[ci][cj-1]==0:
                    isSpreaded=True
                    visited[ci][cj-1]=1
                    grid[ci][cj-1]=2
                    q.put([ci,cj-1])
                if cj+1<c and grid[ci][cj+1]==1 and visited[ci][cj+1]==0:
                    isSpreaded=True
                    visited[ci][cj+1]=1
                    grid[ci][cj+1]=2
                    q.put([ci,cj+1])
            print(grid)
            if isSpreaded==True:
                time=time+1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return -1
        return time

    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.helper(grid)

        