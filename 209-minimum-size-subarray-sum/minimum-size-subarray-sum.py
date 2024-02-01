class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        end=0
        ans=1<<31
        s=0
        while end<len(nums):
            s=s+nums[end]
            if s<target:
                end=end+1
            else:
                while s>=target:
                    ans=min(ans,end-start+1)
                    s=s-nums[start]
                    start=start+1
                end=end+1
        if ans==1<<31:
            return 0
        return ans
        