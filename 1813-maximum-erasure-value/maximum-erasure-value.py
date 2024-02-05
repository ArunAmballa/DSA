class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        preSum=0
        d={}
        s=0
        e=0
        ans=-(1<<31)
        while e<len(nums):
            preSum=preSum+nums[e]
            if nums[e] not in d:
                d[nums[e]]=d.get(nums[e],0)+1
                ans=max(ans,preSum)
                e=e+1
            else:
                while nums[e] in d and s<=e:
                    preSum=preSum-nums[s]
                    d[nums[s]]=d.get(nums[s],0)-1
                    if d[nums[s]]==0:
                        del d[nums[s]]
                    s=s+1
                if nums[e] not in d:
                    d[nums[e]]=d.get(nums[e],0)+1
                    ans=max(ans,preSum)
                e=e+1
        return ans

        