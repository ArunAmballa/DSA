#User function Template for python3

class Solution:
    def helper(self,i,j,arr,dp):
        if i>=j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        ans=1<<31
        for k in range(i,j):
            tempAns=self.helper(i,k,arr,dp)+self.helper(k+1,j,arr,dp)+(arr[i-1]*arr[j]*arr[k])
            ans=min(tempAns,ans)
        dp[i][j]=ans
        return dp[i][j]
    def matrixMultiplication(self, N, arr):
        dp=[[-1 for j in range(N)]for i in range(N)]
        return self.helper(1,N-1,arr,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends