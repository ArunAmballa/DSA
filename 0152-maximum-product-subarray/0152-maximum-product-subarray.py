class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre=1
        suf=1
        maxi=-(1<<31)
        n=len(nums)
        for i in range(0,len(nums)):
            if pre==0:pre=1
            if suf==0:suf=1
            pre=pre*nums[i]
            suf=suf*nums[n-i-1]
            maxi=max(maxi,max(pre,suf))
        return maxi
        