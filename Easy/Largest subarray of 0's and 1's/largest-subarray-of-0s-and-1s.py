#User function Template for python3


# arr[] : the input array containing 0s and 1s
# N : size of the input array

# return the maximum length of the subarray
# with equal 0s and 1s
class Solution:
    def maxLen(self,arr, N):
        d={0:-1}
        ans=0
        currSum=0
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=-1
        for i in range(len(arr)):
            currSum=currSum+arr[i]
            if currSum in d:
                ans=max(ans,i-d[currSum])
            if currSum not in d:
                d[currSum]=i
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends