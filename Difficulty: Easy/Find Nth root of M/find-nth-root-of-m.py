#User function Template for python3
import math
class Solution:
    def findPower(self,a,n):
        x=1;
        for i in range(int(math.log(n,2))+1):
            if(n&1<<i):
                x=x*a
            a=a*a
        return x
        
	def NthRoot(self, n, m):
		lo=1
		hi=m
		while(lo<=hi):
		    mid=(lo+hi)//2
		    k=self.findPower(mid,n)
		    if (k==m):
		        return mid
		    elif (k>m):
		        hi=mid-1
		    else:
		        lo=mid+1
		return -1
		      


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends