class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini=1<<31
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[lo]<=nums[mid]:
                mini=min(mini,nums[lo])
                lo=mid+1
            else:
                mini=min(mini,nums[mid])
                hi=mid-1
        return mini
        