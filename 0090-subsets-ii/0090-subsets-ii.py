class Solution:
    def generate(self,nums,ind,l,ans):
        
        ans.append(l.copy())
        if ind==len(nums):
            return
        for i in range(ind,len(nums)):
            if i>ind and nums[i]==nums[i-1]:
                continue
            l=l+[nums[i]]
            self.generate(nums,i+1,l,ans)
            l.pop()
        return ans
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.generate(nums,0,[],[])
        