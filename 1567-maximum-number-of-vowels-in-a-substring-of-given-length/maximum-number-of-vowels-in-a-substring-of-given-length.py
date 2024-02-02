class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d={'a','e','i','o','u'}
        ans=-(1<<31)
        cnt=0
        for i in range(k):
            if s[i] in d:
                cnt=cnt+1
        ans=max(ans,cnt) 
        for i in range(k,len(s)):
            if s[i-k] in d:
                cnt=cnt-1
            if s[i] in d:
                cnt=cnt+1
            ans=max(ans,cnt) 
        return ans

        