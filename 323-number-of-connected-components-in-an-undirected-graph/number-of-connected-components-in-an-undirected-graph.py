class Solution:
    def dfs(self,source,graph,visited):
        visited[source]=1
        for ne in graph[source]:
            if visited[ne]==0:
                self.dfs(ne,graph,visited)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={i:[] for i in range(n)}
        for edge in edges:
            u,v=edge
            graph[u].append(v)
            graph[v].append(u)
        cnt=0
        visited=[0]*n
        for i in range(n):
            if visited[i]==0:
                self.dfs(i,graph,visited)
                cnt=cnt+1
        return cnt


        