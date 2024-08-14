class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        start=0
        end=0
        maxAnswer=0
        while end<len(s):
            if s[end] not in d:
                d[s[end]]=d.get(s[end],0)+1
                end=end+1
                maxAnswer=max(maxAnswer,len(d))
            else:
                while s[end] in d and start<=end:
                    d[s[start]]=d.get(s[start],0)-1
                    if d[s[start]]==0:
                        del d[s[start]]
                    start=start+1
                d[s[end]]=d.get(s[end],0)+1
                end=end+1
                maxAnswer=max(maxAnswer,len(d))
        return maxAnswer


        