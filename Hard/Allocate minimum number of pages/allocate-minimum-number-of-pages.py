class Solution:
    
    def possible(self,arr,mid):
        students=1
        cnt=0
        for i in range(len(arr)):
            if cnt+arr[i]<=mid:
                cnt=cnt+arr[i]
            else:
                students=students+1
                cnt=arr[i]
        return students
    
    #Function to find minimum number of pages.
    def findPages(self,arr, n, m):
        #Each Student Should get atleast one book
        if m>n:
            return -1
        lo=max(arr)
        hi=sum(arr)
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.possible(arr,mid)<=m:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends