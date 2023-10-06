class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.endOfWord=False
class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
    def insert(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.endOfWord=True
    def complete(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                return False
            else:
                curr=curr.children[c]
                if curr.endOfWord==False:
                    return False
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        obj=Trie()
        for i in range(len(words)):
            obj.insert(words[i])
        ans=""
        for i in range(len(words)):
            if obj.complete(words[i]):
                if len(words[i])>len(ans) or (len(words[i])==len(ans) and words[i]<ans):
                    ans=words[i]
        return ans


        