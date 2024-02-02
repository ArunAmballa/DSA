class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        d={}
        ans=0
        k=3
        for i in range(3):
            d[s[i]]=d.get(s[i],0)+1
        if len(d)==3:
            ans=ans+1
        for i in range(3,len(s)):
            d[s[i-k]]=d.get(s[i-k],0)-1
            if d[s[i-k]]==0:
                del d[s[i-k]]
            d[s[i]]=d.get(s[i],0)+1
            if len(d)==3:
                ans=ans+1
        return ans
