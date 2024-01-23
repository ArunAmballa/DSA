class Solution:
    
    #Function to find minimum number of pages.
    def helper(self,arr,limit):
        student=1
        pages=0
        for i in range(len(arr)):
            if pages+arr[i]<=limit:
                pages=pages+arr[i]
            else:
                student=student+1
                pages=arr[i]
        return student
    def findPages(self,A, N, M):
        if M>N:
            return -1
        lo=max(A)
        hi=sum(A)
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(A,mid)<=M:
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