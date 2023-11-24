class Solution:
    def helper(self,a,b):
        if a==b:
            return True
        if len(a)!=len(b):
            return False
        if (a+" "+b) in self.map:
            return self.map[a+" "+b]
        flag=False
        n=len(a)
        for k in range(1,len(a)):
            if (self.helper(a[:k],b[n-k:]) and self.helper(a[k:],b[:n-k])):
                flag=True
                break
            elif(self.helper(a[:k],b[:k]) and self.helper(a[k:],b[k:])):
                flag=True
                break
        self.map[a+" "+b]=flag
        return self.map[a+" "+b]
    def isScramble(self, s1: str, s2: str) -> bool:
        self.map={}
        return self.helper(s1,s2)