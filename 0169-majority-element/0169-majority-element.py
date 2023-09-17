class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=-(1<<31)
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                el=nums[i]
                cnt=cnt+1
            elif el==nums[i]:
                cnt=cnt+1
            else:
                cnt=cnt-1
        return el
        