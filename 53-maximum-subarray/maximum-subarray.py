class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-(1<<31)
        preSum=0
        for i in range(0,len(nums)):
            preSum=preSum+nums[i]
            ans=max(ans,preSum)
            if preSum<0:
                preSum=0
        return ans
        