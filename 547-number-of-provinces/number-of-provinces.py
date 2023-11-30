class Solution:
    def bfs(self,s,g,vi):
        q=collections.deque()
        q.append(s)
        vi[s]=1
        while q:
            curr=q.popleft()
            for ne in g[curr]:
                if vi[ne]==0:
                    q.append(ne)
                    vi[ne]=1
        return 
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        g={i:[] for i in range(1,len(isConnected)+1)}
        for i in range(0,len(isConnected)):
            for j in range(0,len(isConnected[0])):
                if i!=j and isConnected[i][j]==1:
                    g[i+1].append(j+1)
        print(g)
        n=len(isConnected)
        vi=[0]*(n+1)
        cnt=0
        for i in range(1,n+1):
            if vi[i]==0:
                cnt=cnt+1
                self.bfs(i,g,vi)
        return cnt

