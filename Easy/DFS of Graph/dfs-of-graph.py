#User function Template for python3

class Solution:
    
    def dfs(self,src,adj):
        self.visited[src]=1
        self.ans.append(src)
        for ne in adj[src]:
            if self.visited[ne]==0:
                self.dfs(ne,adj)
    def dfsOfGraph(self, V, adj):
        self.visited=[0]*V
        self.ans=[]
        for i in range(V):
            if self.visited[i]==0:
                self.dfs(i,adj)
        return self.ans


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