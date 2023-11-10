#User function Template for python3
class Solution:
	def minDifference(self, nums, n):
		totalSum=sum(nums)
        N=len(nums)
        dp=[[0 for j in range(totalSum+1)]for i in range(N+1)]
        for i in range(0,N+1):
            for j in range(0,totalSum+1):
                if j==0:
                    dp[i][j]=True
                    continue
                if i==0:
                    dp[i][j]=False
                    continue
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        mini=(1<<31)
        for j in range(0,(totalSum//2)+1):
            if dp[N][j]==True:
                s1=j
                s2=totalSum-s1
                mini=min(mini,abs(s1-s2))
        return mini


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends