from queue import Queue
class Solution:
    def helper(self,graph,numCourses):
        indegree={i:0 for i in range(numCourses)}
        for i in graph:
            for el in graph[i]:
                indegree[el]=indegree[el]+1
        q=Queue()
        visited=[0]*numCourses
        for i in range(numCourses):
            if indegree[i]==0:
                q.put(i)
                visited[i]=1
        cnt=0
        while not q.empty():
            curr=q.get()
            cnt=cnt+1
            for ne in graph[curr]:
                indegree[ne]=indegree[ne]-1
                if visited[ne]==0 and indegree[ne]==0:
                    q.put(ne)
                    visited[ne]=1
        if cnt==numCourses:
            return True
        return False


            



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        for edge in prerequisites:
            u,v=edge
            graph[v].append(u)
        return self.helper(graph,numCourses)
        
        