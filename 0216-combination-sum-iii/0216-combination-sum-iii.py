class Solution:
    def generate(self,candidates,ind,target,k,l,ans):
        if target==0:
            if len(l)==k:
                ans.append(l.copy())
                return 
            return 
        if ind==len(candidates):
            return 
        #Take Case 
        l=l+[candidates[ind]]
        self.generate(candidates,ind+1,target-candidates[ind],k,l,ans)
        l.pop()
        #Not Take Case
        self.generate(candidates,ind+1,target,k,l,ans)
        #Finally return ans
        return ans

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates=[int(x) for x in range(1,10)]
        return self.generate(candidates,0,n,k,[],[])