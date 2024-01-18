class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo=-1
        for i in range(len(nums)):
            if nums[i]==0:
                lo=i
                break

        if lo==-1:
            return nums
        hi=lo+1
        while hi<len(nums):
            if nums[hi]!=0:
                nums[lo],nums[hi]=nums[hi],nums[lo]
                lo=lo+1
                hi=hi+1
            else:
                hi=hi+1
        return nums
        