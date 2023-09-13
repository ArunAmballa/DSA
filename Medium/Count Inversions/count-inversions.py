class Solution:
    def merge(self,nums,lo,mid,hi):
        i=lo
        j=mid+1
        temp=[]
        cnt=0
        while i<=mid and j<=hi:
            if nums[i]<=nums[j]:
                temp.append(nums[i])
                i=i+1
            else:
                temp.append(nums[j])
                cnt=cnt+(mid-i+1)
                j=j+1
        while i<=mid:
            temp.append(nums[i])
            i=i+1
        while j<=hi:
            temp.append(nums[j])
            j=j+1
        for i in range(lo,hi+1):
            nums[i]=temp[i-lo]
        self.ans=self.ans+cnt

    def mergeSort(self,nums,lo,hi):
        if lo>=hi:
            return 
        mid=(lo+hi)//2
        self.mergeSort(nums,lo,mid)
        self.mergeSort(nums,mid+1,hi)
        self.merge(nums,lo,mid,hi)
    def inversionCount(self, arr, n):
        self.ans=0
        self.mergeSort(arr,0,n-1)
        return self.ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends