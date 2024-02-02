class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        c1=[0]*26
        ans=[]
        for i in range(len(p)):
            c=ord(p[i])-97
            c1[c]=c1[c]+1
        c2=[0]*26
        k=len(p)
        for i in range(k):
            c=ord(s[i])-97
            c2[c]=c2[c]+1
        if c1==c2:
            ans.append(i-k+1)
        for i in range(k,len(s)):
            c=ord(s[i-k])-97
            c2[c]=c2[c]-1
            d=ord(s[i])-97
            c2[d]=c2[d]+1
            if c2==c1:
                ans.append(i-k+1)
        return ans       