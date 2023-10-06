class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.endOfword=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.endOfword=True
    def search(self,word,root):
        curr=root
        for i in range(len(word)):
            if word[i]==".":
                for child in curr.children:
                    if self.search(word[i+1:],curr.children[child])==True:
                        return True
                return False
            if word[i] not in curr.children:
                return False
            else:
                curr=curr.children[word[i]]
        return curr.endOfword
class WordDictionary:

    def __init__(self):
        self.obj=Trie()
        
    def addWord(self, word: str) -> None:
        self.obj.insert(word)

    def search(self, word: str) -> bool:
        return self.obj.search(word,self.obj.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)