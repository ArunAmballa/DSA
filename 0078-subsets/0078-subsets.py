class Solution:
    def check(self,nums,i,l,ans):
        if i==len(nums):
            ans.append(l.copy())
            return 
        #Take Case
        l.append(nums[i])
        self.check(nums,i+1,l,ans)
        l.pop()
        # Dont Take Case
        self.check(nums,i+1,l,ans)
        return ans
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.check(nums,0,[],[])
        