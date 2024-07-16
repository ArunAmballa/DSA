class Solution:
    def helper(self,nums,target):
        cnt=0
        st=0
        e=0
        preSum=0
        while e<len(nums):
            preSum=preSum+nums[e]
            if preSum<=target:
                cnt=cnt+(e-st+1)
                e=e+1
            else:
                while preSum>target and st<=e:
                    preSum=preSum-nums[st]
                    st=st+1
                if preSum<=target:
                    cnt=cnt+(e-st+1)
                e=e+1
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans1=self.helper(nums, goal)
        ans2=self.helper(nums,goal-1)
        return ans1-ans2