class Solution:
    def helper(self,s,k):
        st=0
        e=0
        d={}
        ans=0
        while e<len(s):
            d[s[e]]=d.get(s[e],0)+1
            if len(d)<=k:
                ans=ans+(e-st+1)
                e=e+1
            else:
                while len(d)>k and st<=e:
                    d[s[st]]=d.get(s[st],0)-1
                    if d[s[st]]==0:
                        del d[s[st]]
                    st=st+1
                if len(d)==k:
                    ans=ans+(e-st+1)
                e=e+1
        return ans
    def numberOfSubstrings(self, s: str) -> int:
        k=3
        return self.helper(s,k)-self.helper(s,k-1)
        
                
        