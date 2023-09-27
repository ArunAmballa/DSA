class Solution:
    def generate(self,nums,ans,ind):
        if ind==len(nums):
            ans.append(nums.copy())
            return 
        s=set()
        for i in range(ind,len(nums)):
            if (nums[i]) in s:continue
            s.add(nums[i])
            nums[i],nums[ind]=nums[ind],nums[i]
            self.generate(nums,ans,ind+1)
            nums[i],nums[ind]=nums[ind],nums[i]
        return ans
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.generate(nums,[],0)