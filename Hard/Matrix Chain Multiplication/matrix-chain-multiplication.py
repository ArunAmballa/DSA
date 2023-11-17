#User function Template for python3

class Solution:
    def helper(self,i,j,arr):
        if i==j:
            return 0
        ans=1<<31
        for k in range(i,j):
            tempans=self.helper(i,k,arr)+self.helper(k+1,j,arr)+(arr[i-1]*arr[j]*arr[k])
            ans=min(tempans,ans)
        return ans
    def matrixMultiplication(self, N, arr):
        dp=[[-1 for j in range(len(arr))]for i in range(len(arr))]
        # for i in range(0,N):
        #     dp[i][i]=0
        for i in range(N-1,0,-1):
            for j in range(0,N):
                if i>=j:
                    dp[i][j]=0
                    continue
                ans=1<<31
                for k in range(i,j):
                    tempAns=dp[i][k]+dp[k+1][j]+(arr[i-1]*arr[k]*arr[j])
                    ans=min(ans,tempAns)
                dp[i][j]=ans
        return dp[1][N-1] 

        


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