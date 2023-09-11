class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el=0
        cnt=0
        for i in range(len(nums)):
            if cnt==0:
                el=nums[i]
                cnt=cnt+1
            elif nums[i]==el:
                cnt=cnt+1
            else:
                cnt=cnt-1
                if cnt==0:
                    el=0
        return el
        