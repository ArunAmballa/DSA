class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        lo=1
        hi=n-2
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            if arr[mid]>arr[mid-1]:
                lo=mid+1
            else:
                hi=mid-1
        
        