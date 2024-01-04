from queue import Queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}
        for edge in prerequisites:
            u,v=edge
            adj[v].append(u)
        indegree=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j]=indegree[j]+1
        q=Queue()
        for i in range(numCourses):
            if indegree[i]==0:
                q.put(i)
        ans=[]
        while not q.empty():
            curr=q.get()
            ans.append(curr)
            for ne in adj[curr]:
                indegree[ne]=indegree[ne]-1
                if indegree[ne]==0:
                    q.put(ne)
        if len(ans)==numCourses:
            return True
        return False


