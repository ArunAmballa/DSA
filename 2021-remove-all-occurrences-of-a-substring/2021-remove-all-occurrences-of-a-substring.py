class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        found=s.find(part)
        if found==-1:
            return s
        while (s.find(part)!=-1):
            found=s.find(part)
            if found!=-1:
                s=s[:found]+s[found+len(part):]
        return s
        