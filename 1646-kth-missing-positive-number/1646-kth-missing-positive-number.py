class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo=0
        hi=len(arr)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            missings=arr[mid]-(mid+1)
            if missings<k:
                lo=mid+1
            else:
                hi=mid-1
        return lo+k
        