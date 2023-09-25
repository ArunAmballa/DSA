class Solution:
    def generate(self,nums,ind,l,ans):
        if ind==len(nums):
            ans.append(l.copy())
            return 
        #Take Case:
        l=l+[nums[ind]]
        self.generate(nums,ind+1,l,ans)
        l.pop()
        #Not Take
        self.generate(nums,ind+1,l,ans)
        #Return Final Answer
        return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.generate(nums,0,[],[])
        