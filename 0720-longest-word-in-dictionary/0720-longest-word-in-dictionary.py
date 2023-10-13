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
    
    def search(self,word):
        curr=self.root
        for c in word:
            if c in curr.children:
                curr=curr.children[c]
                if curr.endOfWord==False:
                    return False
            else:
                return False
        return curr.endOfWord


class Solution:
    def longestWord(self, words: List[str]) -> str:
        obj=Trie()
        for word in words:
            obj.insert(word)
        ans=""
        for word in words:
            if obj.search(word)==True:
                if (len(word)>len(ans)) or (len(word)==len(ans) and word<ans):
                    ans=word
        return ans

        