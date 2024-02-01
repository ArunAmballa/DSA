class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        d={}
        st=0
        e=0
        ans=-(1<<31)
        while e<len(s):
            if s[e] not in d:
                ans=max(ans,e-st+1)
                d[s[e]]=d.get(s[e],0)+1
                e=e+1
            else:
                while s[e] in d:
                    d[s[st]]=d.get(s[st],0)-1
                    if d[s[st]]==0:
                        del d[s[st]]
                    st=st+1
                ans=max(ans,e-st+1)
                d[s[e]]=d.get(s[e],0)+1
                e=e+1

        return ans


        