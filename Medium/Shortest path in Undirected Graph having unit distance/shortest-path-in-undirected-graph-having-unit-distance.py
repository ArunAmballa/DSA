#User function Template for python3
import math
from queue import Queue
class Solution:
    def bfs(self,src,adj,n):
        visited=[0]*n
        distance=[-1]*n
        q=Queue()
        q.put([src,0])
        visited[src]=1
        while not q.empty():
            curr,dist=q.get()
            distance[curr]=dist
            for ne in adj[curr]:
                if visited[ne]==0:
                    q.put([ne,dist+1])
                    visited[ne]=1
        return distance
            
    def shortestPath(self, edges, n, m, src):
        adj={i:[] for i in range(n)}
        for edge in edges:
            u,v=edge
            adj[u].append(v)
            adj[v].append(u)
        return self.bfs(src,adj,n)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends