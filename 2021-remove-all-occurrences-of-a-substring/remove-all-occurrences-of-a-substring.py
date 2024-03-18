class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s
        ind=s.find(part)
        s=s[:ind]+s[ind+len(part):]
        return self.removeOccurrences(s,part)
        