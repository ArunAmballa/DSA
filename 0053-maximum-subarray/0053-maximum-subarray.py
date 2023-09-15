class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=-(1<<31)
        valSum=0
        for i in range(len(nums)):
            valSum=valSum+nums[i]
            maxi=max(maxi,valSum)
            if valSum<0:
                valSum=0
        return maxi

        