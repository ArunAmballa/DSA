class Solution:
    def generate(self,candidates,ind,target,l,ans):
        if target==0:
            ans.append(l.copy())
            return 
        if ind==len(candidates):
            return 
        for i in range(ind,len(candidates)):
            if i>ind and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break 
            l=l+[candidates[i]]
            self.generate(candidates,i+1,target-candidates[i],l,ans)
            l.pop()
        return ans
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.generate(candidates,0,target,[],[])
        