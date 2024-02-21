class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=-1
        i=0
        while i<len(nums):
            if nums[i]==0:
                ind=i
                break
            else:
                i=i+1
        if ind==-1:
            return 
        j=ind+1
        while j<len(nums):
            if nums[j]!=0:
                nums[ind],nums[j]=nums[j],nums[ind]
                ind=ind+1
                j=j+1
            else:
                j=j+1
        return 
