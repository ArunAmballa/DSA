class Solution:
    def row(self,n):
        ans=1
        l=[]
        l.append(ans)
        for i in range(1,n):
            ans=ans*(n-i)
            ans=ans//i
            l.append(ans)
        return l
    def getRow(self, rowIndex: int) -> List[int]:
        return self.row(rowIndex+1)
        