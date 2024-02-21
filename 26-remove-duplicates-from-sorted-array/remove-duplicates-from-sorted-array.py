class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while j<len(nums):
            if nums[j]==nums[i]:
                j=j+1
            else:
                nums[i+1]=nums[j]
                i=i+1
                j=j+1
                
        return i+1
        