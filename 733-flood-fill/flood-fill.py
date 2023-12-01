from queue import Queue
class Solution:
    def bfs(self,source,image,color,initialColor,visited):
        q=Queue()
        q.put(source)
        sr,sc=source
        visited[sr][sc]=1
        r=len(image)
        c=len(image[0])
        while not q.empty():
            i,j=q.get()
            if i-1>=0 and image[i-1][j]==initialColor and visited[i-1][j]==0:
                q.put([i-1,j])
                visited[i-1][j]=1
                image[i-1][j]=color
            if i+1<r and image[i+1][j]==initialColor and visited[i+1][j]==0:
                q.put([i+1,j])
                visited[i+1][j]=1
                image[i+1][j]=color
            if j-1>=0 and image[i][j-1]==initialColor and visited[i][j-1]==0:
                q.put([i,j-1])
                visited[i][j-1]=1
                image[i][j-1]=color
            if j+1<c and image[i][j+1]==initialColor and visited[i][j+1]==0:
                q.put([i,j+1])
                visited[i][j+1]=1
                image[i][j+1]=color
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initialColor=image[sr][sc]
        visited=[[0 for j in range(len(image[i]))]for i in range(len(image))]
        image[sr][sc]=color
        self.bfs([sr,sc],image,color,initialColor,visited)
        return image

        