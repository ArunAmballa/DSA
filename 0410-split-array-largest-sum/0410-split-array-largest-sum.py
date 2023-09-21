class Solution:
    def possible(self,nums,mid):
        subArrays=1
        subArraySum=0
        for i in range(len(nums)):
            if subArraySum+nums[i]<=mid:
                subArraySum=subArraySum+nums[i]
            else:
                subArrays=subArrays+1
                subArraySum=nums[i]
        return subArrays
    def splitArray(self, nums: List[int], k: int) -> int:
        lo=max(nums)
        hi=sum(nums)
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.possible(nums,mid)<=k:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans
        