class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lo=i+1
            hi=len(nums)-1
            while lo<hi:
                if nums[i]+nums[lo]+nums[hi]==0:
                    ans.append([nums[i],nums[lo],nums[hi]])
                    lo=lo+1
                    hi=hi-1
                    while lo<hi and nums[lo]==nums[lo-1]:lo=lo+1
                    while lo<hi and nums[hi]==nums[hi+1]:hi=hi-1
                elif nums[i]+nums[lo]+nums[hi]>0:
                    hi=hi-1
                else:
                    lo=lo+1
        return ans
        