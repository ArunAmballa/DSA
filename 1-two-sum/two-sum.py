class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        ans=[]
        for i in range(len(nums)):
            a=target-nums[i]
            if a in d:
                return [d[a],i]
            else:
                d[nums[i]]=i


