import math
class Solution:
    def rightmost(self,xor):
        for i in range(0,32):
            if xor&(1<<i)!=0:
                return i
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor=0
        for i in range(len(nums)):
            xor=xor^nums[i]
        index=self.rightmost(xor)
        xor1=0
        xor2=0
        for i in range(len(nums)):
            if nums[i]&(1<<index)!=0:
                xor1=xor1^nums[i]
            else:
                xor2=xor2^nums[i]
        return [xor1,xor2]
