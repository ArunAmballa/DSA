class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        ans=0
        m=int(1e9)+7
        while l<=r:
            if nums[l]+nums[r]>target:
                r=r-1
            else:
                ans=ans+(1<<(r-l))
                l=l+1
        return ans%m
        