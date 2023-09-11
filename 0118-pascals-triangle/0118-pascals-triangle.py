class Solution:
    def row(self,n):
        l=[]
        ans=1
        l.append(ans)
        for i in range(1,n):
            ans=ans*(n-i)
            ans=ans//i
            l.append(ans)
        return l
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            ans.append(self.row(i))
        return ans
        
        