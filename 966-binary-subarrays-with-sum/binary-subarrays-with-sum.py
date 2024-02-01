class Solution:
    def helper(self,nums,goal):
        s=0
        e=0
        ans=0
        preSum=0
        while e<len(nums):
            preSum=preSum+nums[e]
            if preSum<=goal:
                ans=ans+ (e-s+1)
                e=e+1
            else:
                while preSum > goal and s<=e:
                    preSum=preSum-nums[s]
                    s=s+1
                ans+=e-s+1
                e=e+1
        return ans

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans1=self.helper(nums,goal)
        ans2=self.helper(nums,goal-1)
        return ans1-ans2

        