class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        n=len(nums)
        while j<n:
            if nums[j]==nums[i]:
                j=j+1
            else:
                i=i+1
                nums[i]=nums[j]
                j=j+1
        return i+1
        