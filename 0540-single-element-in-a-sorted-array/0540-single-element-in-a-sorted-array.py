class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo=0
        n=len(nums)
        hi=n-1
        #You will forget this edge case
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:return nums[0]
        if nums[n-1]!=nums[n-2]:return nums[n-1]
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid%2==0:
                if nums[mid]==nums[mid-1]:
                    hi=mid-1
                elif nums[mid]==nums[mid+1]:
                    lo=mid+1
            else:
                if nums[mid]==nums[mid+1]:
                    hi=mid-1
                elif nums[mid]==nums[mid-1]:
                    lo=mid+1
        

        