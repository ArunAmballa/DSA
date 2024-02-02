class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=-(1<<31)
        preSum=0
        for i in range(k):
            preSum=preSum+nums[i]
        ans=max(ans,preSum/k)
        for i in range(k,len(nums)):
            preSum=preSum-nums[i-k]
            preSum=preSum+nums[i]
            ans=max(ans,preSum/k)
        return ans

        