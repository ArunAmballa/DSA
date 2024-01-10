#User function Template for python3
import math
import heapq
from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        n=len(grid)
        m=len(grid[0])
        distance=[[math.inf for j in range(m)]for i in range(n)]
        h=[]
        if source==destination:
            return 0
        i,j=source
        if grid[i][j]==0:
            return -1
        heapq.heappush(h,[0,i,j])
        while h:
            dist,r,c=heapq.heappop(h)
            if r+1<n and grid[r+1][c]==1 and distance[r+1][c]>dist+1:
                distance[r+1][c]=dist+1
                heapq.heappush(h,[dist+1,r+1,c])
            if r-1>=0 and grid[r-1][c]==1 and distance[r-1][c]>dist+1:
                distance[r-1][c]=dist+1
                heapq.heappush(h,[dist+1,r-1,c])
            if c+1<m and grid[r][c+1]==1 and distance[r][c+1]>dist+1:
                distance[r][c+1]=dist+1
                heapq.heappush(h,[dist+1,r,c+1])
            if c-1>=0 and grid[r][c-1]==1 and distance[r][c-1]>dist+1:
                distance[r][c-1]=dist+1
                heapq.heappush(h,[dist+1,r,c-1])
        m,n=destination
        if distance[m][n]==math.inf:
            return -1
        return distance[m][n]
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

         
if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int,input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int,input().strip().split())
        obj=Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends