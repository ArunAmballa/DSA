class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        l=0
        r=k-1
        res=(1<<31)
        while r<len(nums):
            res=min(res,nums[r]-nums[l])
            l=l+1
            r=r+1
        return res
        