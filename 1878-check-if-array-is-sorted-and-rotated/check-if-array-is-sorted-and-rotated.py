class Solution:
    def check(self, nums: List[int]) -> bool:
      breakPoints=0
      for i in range(0,len(nums)):
        if nums[i-1]>nums[i]:
          breakPoints=breakPoints+1
      return True if breakPoints<=1 else False
        