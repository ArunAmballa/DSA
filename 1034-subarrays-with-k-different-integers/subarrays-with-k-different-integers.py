class Solution:
    def helper(self,nums,k):
        s=0
        e=0
        d={}
        ans=0
        while e<len(nums):
            d[nums[e]]=d.get(nums[e],0)+1
            if len(d)<=k:
                ans=ans+(e-s+1)
                e=e+1
            else:
                while len(d)>k:
                    d[nums[s]]=d.get(nums[s],0)-1
                    if d[nums[s]]==0:
                        del d[nums[s]]
                    s=s+1
                if len(d)==k:
                    ans=ans+(e-s+1)
                e=e+1
        return ans 

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k)-self.helper(nums,k-1)
             