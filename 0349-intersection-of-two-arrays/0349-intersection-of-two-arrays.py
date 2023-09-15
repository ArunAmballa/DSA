class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        n=len(a)
        m=len(b)
        i=0
        j=0
        a.sort()
        b.sort()
        if n==0:
            return b
        if m==0:
            return a
        temp=[]
        while i<n and j<m:
            if a[i]==b[j]:
                if temp and temp[-1]!=a[i]:
                    temp.append(a[i])
                elif not temp:
                    temp.append(a[i])
                i=i+1
                j=j+1
            elif a[i]<b[j]:
                i=i+1
            else:
                j=j+1
        return temp

        