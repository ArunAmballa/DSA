class Solution:
    def backtrack(self,n,openc,closec,l,ans):
        if openc==closec==n:
            ans.append("".join(l))
            return
        if openc<n:
            l.append("(")
            self.backtrack(n,openc+1,closec,l,ans)
            l.pop()
        
        if closec<openc:
            l.append(")")
            self.backtrack(n,openc,closec+1,l,ans)
            l.pop()
        
        return ans

    def generateParenthesis(self, n: int) -> List[str]:
        return self.backtrack(n,0,0,[],[])
        