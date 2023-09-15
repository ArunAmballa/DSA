#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        d={0:-1}
        maxLen=0
        preSum=0
        for i in range(len(arr)):
            preSum=preSum+arr[i]
            target=preSum-k
            if target in d:
                maxLen=max(maxLen,i-d[target])
            if preSum not in d:
                d[preSum]=i
        return maxLen
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends