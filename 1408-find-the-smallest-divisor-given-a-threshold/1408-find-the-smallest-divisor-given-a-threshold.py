class Solution:
    def helper(self,nums,mid):
        cnt=0
        for i in range(len(nums)):
            cnt=cnt+math.ceil(nums[i]/mid)
        return cnt
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo=1
        hi=max(nums)
        ans=max(nums)
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.helper(nums,mid)<=threshold:
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans