#User function Template for python3
from queue import Queue
class Solution:
    def bfs(self,source,graph,visited):
        q=Queue()
        q.put(source)
        visited[source]=1
        while not q.empty():
            curr=q.get()
            for ne in graph[curr]:
                if visited[ne]==0:
                    q.put(ne)
                    visited[ne]=1
    def numProvinces(self, adj, V):
        graph={i:[] for i in range(V)}
        for i in range(len(adj)):
            for j in range(len(adj[i])):
                if i!=j and adj[i][j]==1:
                    graph[i].append(j)
        
        visited=[0]*V
        cnt=0
        for i in range(V):
            if visited[i]==0:
                self.bfs(i,graph,visited)
                cnt=cnt+1
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends