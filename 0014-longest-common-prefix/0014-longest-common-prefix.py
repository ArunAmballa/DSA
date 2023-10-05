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
        return
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        obj=Trie()
        for i in range(len(strs)):
            obj.insert(strs[i])
        res=""
        root=obj.root
        while root:
            if len(root.children)>1 or root.endOfWord:
                return res
            keys=list(root.children.keys())
            key=keys[0]
            res=res+key
            root=root.children[key]
        return res

