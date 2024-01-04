from typing import List
from queue import Queue
class Solution:
    
    def bfs(self,src,adj):
        q=Queue()
        q.put(src)
        self.visited[src]=1
        while not q.empty():
            curr=q.get()
            for ne in adj[curr]:
                if self.visited[ne]==0:
                    q.put(ne)
                    self.visited[ne]=1
                    self.parent[ne]=curr
                else:
                    if ne!=self.parent[curr]:
                        return True
        return False
        
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		self.visited=[0]*V
		self.parent={}
		for i in range(V):
		    if self.visited[i]==0:
		        self.parent[i]=-1
		        ans=self.bfs(i,adj)
		        if ans==True:
		            return True
		return False
		


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