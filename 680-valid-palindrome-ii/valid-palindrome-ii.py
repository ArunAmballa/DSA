class Solution:
    def checkPalindrome(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i=i+1
            j=j-1
        return True
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1

        while i<j:
            if s[i]==s[j]:
                i=i+1
                j=j-1
            else:
                return self.checkPalindrome(s,i+1,j) or self.checkPalindrome(s,i,j-1)
        return True

        