class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre=1
        suf=1
        maxi=-(1<<31)
        n=len(nums)
        for i in range(len(nums)):
            if pre==0:pre=1
            if suf==0:suf=1
            pre=pre*nums[i]
            suf=suf*nums[n-1-i]
            maxi=max(maxi,max(pre,suf))
        return maxi
        