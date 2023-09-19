#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        lo=0
        hi=n-1
        mini=1<<31
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if arr[lo]<=arr[mid]:
                if arr[lo]<mini:
                    mini=arr[lo]
                    ans=lo
                lo=mid+1
            else:
                if arr[mid]<mini:
                    mini=arr[mid]
                    ans=mid
                hi=mid-1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends