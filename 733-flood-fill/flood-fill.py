class Solution:
    def bfs(self,r,c,image,m,n,vis,co,ic):
        q=collections.deque()
        q.append([r,c])
        vis[r][c]=co
        while q:
            row,col=q.popleft()
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i==1 and j==1) or (i==-1 and j==-1) or (i==-1 and j==1) or (i==1 and j==-1):
                        pass
                    else:
                        nrow=row+i
                        ncol=col+j
                        if (nrow>=0 and nrow<m and ncol>=0 and ncol<n and image[nrow][ncol]==ic and vis[nrow][ncol]==-1):
                            q.append([nrow,ncol])
                            vis[nrow][ncol]=co
                            
        return 
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        vis=[[-1 for j in range(n)]for i in range(m)]
        ic=image[sr][sc]
        self.bfs(sr,sc,image,m,n,vis,color,ic)
    
        for i in range(0,m):
            for j in range(0,n):
                if vis[i][j]!=color:
                    vis[i][j]=image[i][j]
        return vis

        