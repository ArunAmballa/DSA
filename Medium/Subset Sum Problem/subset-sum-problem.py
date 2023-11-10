#User function Template for python3

class Solution:
    # def helper(self,arr,w,n,dp):
    #     if w==0:
    #         return True
    #     if n==0:
    #         return False
    #     if dp[n][w]!=-1:
    #         return dp[n][w]
    #     if arr[n-1]<=w:
    #         dp[n][w]=self.helper(arr,w-arr[n-1],n-1,dp) or self.helper(arr,w,n-1,dp)
    #     else:
    #         dp[n][w]=self.helper(arr,w,n-1,dp)
    #     return dp[n][w]
    # dp=[[0 for j in range(sum+1)]for i in range(N+1)]
    #     for i in range(0,N+1):
    #         for j in range(0,sum+1):
    #             if j==0:
    #                 dp[i][j]=True
    #                 continue
    #             if i==0:
    #                 dp[i][j]=False
    #                 continue
    #             if arr[i-1]<=j:
    #                 dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
    #             else:
    #                 dp[i][j]=dp[i-1][j]
    #     return dp[N][sum]
    def isSubsetSum (self, N, arr, sum):
        prev=[0]*(sum+1)
        curr=[0]*(sum+1)
        for i in range(0,N+1):
            for j in range(0,sum+1):
                if j==0:
                    prev[j]=True
                    continue
                if i==0:
                    prev[j]=False
                    continue
                if arr[i-1]<=j:
                    curr[j]=prev[j-arr[i-1]] or prev[j]
                else:
                   curr[j]=prev[j]
            prev=curr[:]
        return curr[sum]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends