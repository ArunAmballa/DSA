class Solution:
    
    #Function to return list containing vertices in Topological order.
    def dfs(self,src,adj):
        self.visited[src]=1
        for ne in adj[src]:
            if self.visited[ne]==0:
                self.dfs(ne,adj)
        self.st.append(src)
    def topoSort(self, V, adj):
        self.st=[]
        self.visited=[0]*V
        for i in range(V):
            if self.visited[i]==0:
                self.dfs(i,adj)
        ans=[]
        while self.st:
            a=self.st.pop()
            ans.append(a)
        return ans
        
            



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends