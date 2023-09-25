class Solution:
    def generate(self,candidates,ind,target,l,ans):
        if target==0:
            ans.append(l.copy())
            return 
        if target<0:
            return 
        for i in range(ind,len(candidates)):
            l=l+[candidates[i]]
            self.generate(candidates,i,target-candidates[i],l,ans)
            l.pop()
        return ans

        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.generate(candidates,0,target,[],[])
        