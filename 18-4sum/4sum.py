class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for j in range(len(nums)-3):
            if j>0 and nums[j]==nums[j-1]:
                continue
            for i in range(j+1,len(nums)-2):
                if i>j+1 and nums[i]==nums[i-1]:
                    continue
                lo=i+1
                hi=len(nums)-1
                while lo<hi:
                    if nums[j]+nums[i]+nums[lo]+nums[hi]==target:
                        ans.append([nums[j],nums[i],nums[lo],nums[hi]])
                        lo=lo+1
                        hi=hi-1
                        while lo<hi and nums[lo]==nums[lo-1]:lo=lo+1
                        while lo<hi and nums[hi]==nums[hi+1]:hi=hi-1
                    elif nums[j]+nums[i]+nums[lo]+nums[hi]>target:
                        hi=hi-1
                    else:
                        lo=lo+1
        return ans
        