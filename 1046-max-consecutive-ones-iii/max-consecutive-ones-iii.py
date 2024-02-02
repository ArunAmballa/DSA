class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s=0
        e=0
        cnt=0
        ans=-(1<<31)
        while e<len(nums):
            if nums[e]==0:
                cnt=cnt+1
            if cnt<=k:
                ans=max(ans,e-s+1)
                e=e+1
            else:
                while cnt>k and s<=e:
                    if nums[s]==0:
                        cnt=cnt-1
                    s=s+1
                if cnt<=k:
                    ans=max(ans,e-s+1)
                e=e+1
        return ans
        