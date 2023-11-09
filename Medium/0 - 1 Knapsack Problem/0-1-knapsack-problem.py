#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def helper(self,wt,val,W,n,dp):
        if n==0 or W==0:
            return 0
        if dp[n][W]!=-1:
            return dp[n][W]
        if wt[n-1]<=W:
            dp[n][W]=max((val[n-1]+self.helper(wt,val,W-wt[n-1],n-1,dp)),self.helper(wt,val,W,n-1,dp))
        else:
            dp[n][W]=self.helper(wt,val,W,n-1,dp)
        return dp[n][W]
    def knapSack(self,W, wt, val, n):
        dp=[[0 for j in range(W+1)]for i in range(n+1)]
        for i in range(0,n+1):
            for j in range(0,W+1):
                if i==0 or j==0:
                    dp[i][j]=0
                    continue
                if wt[i-1]<=j:
                    dp[i][j]=max((val[i-1]+dp[i-1][j-wt[i-1]]),dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][W]
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends