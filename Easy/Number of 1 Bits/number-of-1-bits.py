#User function Template for python3
import math
class Solution:
	def setBits(self, n):
		cnt=0
		for i in range(0,int(math.log(n,2))+1):
		    if n&(1<<i)!=0:
		        cnt=cnt+1
		return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends