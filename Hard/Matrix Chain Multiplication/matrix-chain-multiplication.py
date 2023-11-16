#User function Template for python3

class Solution:
    
    def matrixMultiplication(self, N, arr):
        # code here
        dp=[[-1 for j in range(len(arr))]for i in range(len(arr))]
        def helper(i,j,arr):
            if i>=j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans=1<<31
            for k in range(i,j):
                tempAns=helper(i,k,arr)+helper(k+1,j,arr)+(arr[i-1]*arr[k]*arr[j])
                ans=min(ans,tempAns)
            dp[i][j]=ans
            return dp[i][j]
        return helper(1,len(arr)-1,arr)
        


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