import heapq
import math
from queue import Queue
class Solution:

    
    def dijkstra(self, V, adj, S):
        distance=[math.inf]*V
        h=[]
        heapq.heappush(h,[0,S])
        distance[S]=0
        while h:
            dist,curr=heapq.heappop(h)
            for ne in adj[curr]:
                if distance[ne[0]]> dist + ne[1]:
                    distance[ne[0]]=dist+ne[1]
                    heapq.heappush(h,[distance[ne[0]],ne[0]])
        return distance
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends