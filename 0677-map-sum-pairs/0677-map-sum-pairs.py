class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.count=0
class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
        self.map={}
    def insert(self,word,val):
        change=val-self.map.get(word,0)
        self.map[word]=val
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
            curr.count=curr.count+change
        
    def check(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                return 0
            curr=curr.children[c]
        return curr.count
            
class MapSum:

    def __init__(self):
        self.obj=Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.obj.insert(key,val)
        

    def sum(self, prefix: str) -> int:
        return self.obj.check(prefix)

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)