class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi=-(1<<31)
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count=count+1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi if maxi!=-(1<<31) else 0
        