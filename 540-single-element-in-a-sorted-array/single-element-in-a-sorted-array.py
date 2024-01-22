class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        if len(nums)==1:
            return nums[0]
        if nums[lo]!=nums[lo+1]:
            return nums[lo]
        if nums[hi]!=nums[hi-1]:
            return nums[hi]
        
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif nums[mid]==nums[mid-1]:
                if mid&1==0:hi=mid-1
                else:lo=mid+1
            elif nums[mid]==nums[mid+1]:
                if mid&1==0:lo=mid+1
                else:hi=mid-1
        
        
        