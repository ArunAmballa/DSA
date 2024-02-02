class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        e=0
        ans=1<<31
        preSum=0
        while e<len(nums):
            preSum=preSum+nums[e]
            if preSum<target:
                e=e+1
            else:
                while preSum>=target and s<=e:
                    ans=min(ans,e-s+1)
                    preSum=preSum-nums[s]
                    s=s+1
                e=e+1
        return ans if ans!=1<<31 else  0        