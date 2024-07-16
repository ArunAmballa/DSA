class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d={}
        st=0
        e=0
        ans=0
        while e<len(s):
            d[s[e]]=d.get(s[e],0)+1
            if len(d)<=k:
                ans=max(ans,e-st+1)
            while len(d)>k:
                d[s[st]]=d[s[st]]-1
                if(d[s[st]]==0):
                    del d[s[st]]
                st=st+1
            e=e+1
        return ans





        