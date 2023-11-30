#User function Template for python3

class Solution:
    def dfs(self,source,adj,visited):
        visited[source]=1
        self.depth.append(source)
        for ne in adj[source]:
            if visited[ne]==0:
                self.dfs(ne,adj,visited)
        
    def dfsOfGraph(self, V, adj):
        self.depth=[]
        visited=[0]*V
        self.dfs(0,adj,visited)
        return self.depth



#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends