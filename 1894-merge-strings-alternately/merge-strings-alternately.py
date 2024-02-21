class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        ans=""
        while i<len(word1) and j<len(word2):
            ans=ans+word1[i]
            ans=ans+word2[j]
            i=i+1
            j=j+1
        while i<len(word1):
            ans=ans+word1[i]
            i=i+1
        while j<len(word2):
            ans=ans+word2[j]
            j=j+1
        return ans