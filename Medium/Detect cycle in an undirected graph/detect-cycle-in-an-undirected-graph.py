from typing import List
from queue import Queue
class Solution:
    def bfs(self,source,adj,visited,parent):
        q=Queue()
        q.put(source)
        visited[source]=1
        parent[source]=-1
        while not q.empty():
            curr=q.get()
            for ne in adj[curr]:
                if visited[ne]==0:
                    q.put(ne)
                    visited[ne]=1
                    parent[ne]=curr
                else:
                    if parent[curr]!=ne:
                        return True
        return False
                    
                    
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		visited=[0]*V
		parent={}
		ans=False
		for i in range(V):
		    if visited[i]==0:
		        ans=self.bfs(i,adj,visited,parent)
		        if ans==True:
		            break
		return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends