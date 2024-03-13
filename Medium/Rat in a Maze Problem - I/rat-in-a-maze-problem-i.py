#User function Template for python3

class Solution:
    def helper(self,row,col,m,n,s,visited):
        if row==n-1 and col==n-1:
            self.ans.append(s)
            return 
        if((row+1 < n) and m[row+1][col]!=0 and visited[row+1][col]==0):
            s=s+"D"
            visited[row+1][col]=1
            self.helper(row+1,col,m,n,s,visited)
            visited[row+1][col]=0
            q=len(s)
            s=s[:q-1]
        if((row-1 >= 0) and m[row-1][col]!=0 and visited[row-1][col]==0):
            s=s+"U"
            visited[row-1][col]=1
            self.helper(row-1,col,m,n,s,visited)
            visited[row-1][col]=0
            q=len(s)
            s=s[:q-1]
        if((col-1 >= 0) and m[row][col-1]!=0 and visited[row][col-1]==0):
            s=s+"L"
            visited[row][col-1]=1
            self.helper(row,col-1,m,n,s,visited)
            visited[row][col-1]=0
            q=len(s)
            s=s[:q-1]
        if((col+1 <n ) and m[row][col+1]!=0 and visited[row][col+1]==0):
            s=s+"R"
            visited[row][col+1]=1
            self.helper(row,col+1,m,n,s,visited)
            visited[row][col+1]=0
            q=len(s)
            s=s[:q-1]
        
        
    def findPath(self, m, n):
        self.ans=[]
        if m[0][0]==0:
            return []
        s=""
        visited=[[0 for i in range(n)]for j in range(n)]
        visited[0][0]=1
        self.helper(0,0,m,n,s,visited)
        return self.ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends