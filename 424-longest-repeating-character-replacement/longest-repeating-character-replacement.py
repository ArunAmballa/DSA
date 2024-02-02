class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        st=0
        e=0
        l=[0]*26
        ans=-(1<<31)
        while e<len(s):
            c=ord(s[e])-65
            l[c]=l[c]+1
            max_char=max(l)
            if ((e-st+1)-max_char)<=k:
                ans=max(ans,e-st+1)
                e=e+1
            else:
                d=ord(s[st])-65
                l[d]=l[d]-1
                st=st+1
                e=e+1
        return ans

            

        