class Solution:
    def helper(self,nums,k):
        s=0
        e=0
        cnt=0
        ans=0
        while e<len(nums):
            if nums[e]%2!=0:
                cnt=cnt+1
            if cnt<=k:
                ans=ans+(e-s+1)
                e=e+1
            else:
                while cnt>k and s<=e:
                    if nums[s]%2!=0:
                        cnt=cnt-1
                    s=s+1
                if cnt<=k:
                    ans=ans+(e-s+1)
                e=e+1
        return ans
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k)-self.helper(nums,k-1)