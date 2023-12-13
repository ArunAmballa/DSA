#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    def bfs(self,src,adj):
        q=Queue()
        visited=[0]*len(adj)
        q.put(src)
        ans=[]
        visited[src]=1
        while not q.empty():
            curr=q.get()
            ans.append(curr)
            for ne in adj[curr]:
                if visited[ne]==0:
                    q.put(ne)
                    visited[ne]=1
        return ans
            
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        return self.bfs(0,adj)


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends