class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(0,n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=0-nums[i]
            lo=i+1
            hi=n-1
            while lo<hi:
                if nums[lo]+nums[hi]==target:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    while lo<hi and nums[lo]==nums[lo+1]:lo=lo+1
                    while lo<hi and nums[hi]==nums[hi-1]:hi=hi-1
                    lo=lo+1
                    hi=hi-1
                elif nums[lo]+nums[hi]>target:
                    hi=hi-1
                else:
                    lo=lo+1
        return ans
        