class Solution:
    def ceil(self,nums,target):
        lo=0
        hi=len(nums)-1
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                ans=mid
                hi=mid-1
            elif target>nums[mid]:
                lo=mid+1
            else:
                hi=mid-1
        return ans
    def floor(self,nums,target):
        lo=0
        hi=len(nums)-1
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                ans=mid
                lo=mid+1
            elif target>nums[mid]:
                lo=mid+1
            else:
                hi=mid-1
        return ans
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=self.ceil(nums,target)
        b=self.floor(nums,target)
        return [a,b]

        