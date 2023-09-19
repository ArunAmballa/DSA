class Solution:
    def ceilBinary(self,nums,target):
        ans=-1
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                ans=mid
                hi=mid-1
            elif target<nums[mid]:
                hi=mid-1
            else:
                lo=mid+1
        return ans
    def floorBinary(self,nums,target):
        ans=-1
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                ans=mid
                lo=mid+1
            elif target<nums[mid]:
                hi=mid-1
            else:
                lo=mid+1
        return ans
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.ceilBinary(nums,target)
        last=self.floorBinary(nums,target)
        return [first,last]
        