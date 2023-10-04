class TrieNode:
    def __init__(self):
        self.children=[None]*26
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        cnt=0
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.children[index]==None:
                curr.children[index]=TrieNode()
                cnt=cnt+1
            curr=curr.children[index]
        return cnt
class Solution:
    def countDistinct(self, s: str) -> int:
        obj=Trie()
        ans=0
        for i in range(len(s)):
            ans=ans+obj.insert(s[i:])
        return ans
        