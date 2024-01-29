#User function Template for python3
class Solution:
    def maximumSumSubarray (self,k,arr,n):
        s=0
        ans=-1<<31
        for i in range(k):
            s=s+arr[i]
        ans=max(ans,s)
        for i in range(k,len(arr)):
            s=s-arr[i-k]
            s=s+arr[i]
            ans=max(ans,s)
        return ans
        
       





#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends