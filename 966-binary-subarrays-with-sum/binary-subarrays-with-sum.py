class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d={0:1}
        preSum=0
        ans=0
        for i in range(len(nums)):
            preSum=preSum+nums[i]
            target=preSum-goal
            if target in d:
                ans=ans+d[target]
            d[preSum]=d.get(preSum,0)+1
        return ans
