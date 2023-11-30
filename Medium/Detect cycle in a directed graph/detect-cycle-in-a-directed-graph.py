#User function Template for python3


class Solution:
    def dfs(self,source,adj,visited,stackFrame):
        visited[source]=1
        stackFrame[source]=1
        for ne in adj[source]:
            if visited[ne]==0:
                if self.dfs(ne,adj,visited,stackFrame)==True:
                    return True
            else:
                if stackFrame[ne]==1:
                    return True
        stackFrame[source]=0
        return False
    def isCyclic(self, V, adj):
        visited=[0]*V
        stackFrame={}
        ans=False
        for i in range(V):
            if visited[i]==0:
                ans=self.dfs(i,adj,visited,stackFrame)
                if ans==True:
                    break
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends