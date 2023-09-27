class Solution:
    def generate(self,nums,ans,ind):
        if ind==len(nums):
            ans.append(nums.copy())
            return 
        for i in range(ind,len(nums)):
            nums[i],nums[ind]=nums[ind],nums[i]
            self.generate(nums,ans,ind+1)
            nums[i],nums[ind]=nums[ind],nums[i]
        return ans
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.generate(nums,[],0)
        