class Solution:
    def generate(self,candidates,target,ind,l,ans):
        if target==0:
            ans.append(l.copy())
            return 
        if target<0 or ind==len(candidates):
            return 
        #Take Case 
        l=l+[candidates[ind]]
        self.generate(candidates,target-candidates[ind],ind,l,ans)
        l.pop()
        #Not Take Case
        self.generate(candidates,target,ind+1,l,ans)
        # final return ans
        return ans


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.generate(candidates,target,0,[],[])
        