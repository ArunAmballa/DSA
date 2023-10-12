#User function Template for python3

class Solution:
	def AllPrimeFactors(self, N):
		l=[]
		for i in range(2,N+1):
		    while N%i==0:
		        if len(l)==0:
		            l.append(i)
		        elif len(l)!=0 and l[-1]!=i:
		            l.append(i)
		        N=N/i
		    if N==1:
		        break
		return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends