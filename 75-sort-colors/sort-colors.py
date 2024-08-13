class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIndex=0
        arrayLength=len(nums)
        twoIndex=arrayLength-1
        index=0
        while index <=twoIndex:
            if nums[index]==2:
                nums[index],nums[twoIndex]=nums[twoIndex],nums[index]
                twoIndex=twoIndex-1
            elif nums[index]==0:
                nums[index],nums[zeroIndex]=nums[zeroIndex],nums[index]
                index=index+1
                zeroIndex=zeroIndex+1
            else:
                index=index+1
        return 
        