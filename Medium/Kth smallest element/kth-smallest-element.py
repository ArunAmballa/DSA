#User function Template for python3

class Solution:
    def partition(self,nums,lo,hi):
        pivot=nums[lo]
        i=lo
        j=hi
        while i<j:
            while i<hi and nums[i]<=pivot:
                i=i+1
            while j>lo and nums[j]>pivot:
                j=j-1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
        nums[lo],nums[j]=nums[j],nums[lo]
        return j
    def QuickSelect(self,nums,lo,hi,k):
        pIndex=self.partition(nums,lo,hi)
        if pIndex==k:
            return nums[pIndex]
        elif k<pIndex:
            return self.QuickSelect(nums,lo,pIndex-1,k)
        else:
            return self.QuickSelect(nums,pIndex+1,hi,k)
    def kthSmallest(self,arr, l, r, k):
        return self.QuickSelect(arr,0,r,k-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends