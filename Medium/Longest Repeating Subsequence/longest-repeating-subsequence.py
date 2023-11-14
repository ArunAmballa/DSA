#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, str):
		n=len(str)
        m=len(str)
        x=str
        y=str
        # dp=[[-1 for j in range(m+1)]for i in range(n+1)]
        prev=[-1]*(m+1)
        for i in range(0,n+1):
            curr=[-1]*(m+1)
            for j in range(0,m+1):
                if i==0 or j==0:
                    curr[j]=0
                    continue
                if x[i-1]==y[j-1] and i!=j:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev=curr
        return curr[m]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends